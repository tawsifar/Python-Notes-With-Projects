# note: topics 61, 61B, 62, 63 and 64 were added later by me. the comments in these topics only were written by AI, and I reviewed them multiple times myself. I think they are good enough to explain everything clearly.

# production basics = the habits that separate a "works on my laptop" script from real software
# 1) configuration  = settings that change between machines (api keys, timeouts, log level)
# 2) secrets        = configuration that must stay private (api keys, passwords, tokens)
# 3) logging        = a proper record of what your program did, instead of print()
#
# golden rule: CODE goes to git, SECRETS never go to git
# a key hard-coded in a public repo gets found by automatic bots, often within minutes
# install: uv add pydantic-settings python-dotenv requests
#          (pydantic-settings installs pydantic too)
# needs python 3.10+

import os
import sys
import logging
import tempfile
from functools import lru_cache
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Literal

import requests
from pydantic import Field, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


# PART 1: environment variables (the basic idea)
# an environment variable = a named value that lives OUTSIDE your code, in the operating system
# your code reads it at runtime, so the same code works on every machine with different values
#
# how to set one in a terminal (only for that terminal window):
#   Windows PowerShell:   $env:WEATHER_API_KEY = "abc123"
#   Windows cmd:          set WEATHER_API_KEY=abc123
#   Linux / Mac:          export WEATHER_API_KEY=abc123
#
# how to read it in python:
#   os.environ["NAME"]        -> KeyError if missing (loud, good when it is required)
#   os.getenv("NAME")         -> returns None if missing (quiet)
#   os.getenv("NAME", "x")    -> returns "x" if missing (a default value)

def demo_env_vars() -> None:
    os.environ["DEMO_NAME"] = "Tawsif"        # set one just for this running program
    print(os.environ["DEMO_NAME"])            # Tawsif
    print(os.getenv("DOES_NOT_EXIST"))        # None
    print(os.getenv("DOES_NOT_EXIST", "fallback"))   # fallback

    # IMPORTANT: environment variables are ALWAYS strings
    os.environ["MAX_TRIES"] = "5"
    tries = int(os.getenv("MAX_TRIES", "3"))  # convert yourself, or let pydantic-settings do it
    print(tries + 1)                          # 6
    # booleans are even trickier: bool("False") is True because the string is not empty!
    # pydantic-settings (Part 3) understands "true", "false", "1", "0" correctly

    del os.environ["DEMO_NAME"]               # remove it again
    del os.environ["MAX_TRIES"]


# PART 2: the .env file and .gitignore
# typing variables in the terminal every time is annoying, so we use a file named .env
# it sits in your project folder, one NAME=value per line, no spaces around =, no quotes needed
#
# example .env  (this file is PRIVATE, never commit it):
#   WEATHER_API_KEY=your_real_key_here
#   LOG_LEVEL=INFO
#   REQUEST_TIMEOUT=10
#
# the .gitignore file tells git which files to NEVER track
# example .gitignore (create it BEFORE your first commit):
#   .env
#   .env.*
#   !.env.example
#   .venv/
#   __pycache__/
#   *.log
#
# .env.example = a safe copy with FAKE values that you DO commit
# it shows other people (and future you) which variables the project needs:
#   WEATHER_API_KEY=put_your_key_here
#   LOG_LEVEL=INFO
#   REQUEST_TIMEOUT=10
#
# IMPORTANT: .gitignore only stops FUTURE tracking
# if .env was already committed once, add it to .gitignore AND run:  git rm --cached .env
#
# loading a .env file with python-dotenv (the simple way):
#   from dotenv import load_dotenv
#   load_dotenv()                    # reads .env and puts the values into os.environ
#   key = os.getenv("WEATHER_API_KEY")
# by default a REAL environment variable wins over the .env value (override=False)
# on a real server (Docker, cloud hosting) you set the variables in the platform's settings,
# you do not upload a .env file


# PART 3: pydantic-settings (the better way, recommended)
# it loads config from environment variables AND .env, converts types, and validates everything
# if something is missing or wrong, the program stops at startup with a clear message
# (much better than crashing later in the middle of a request)
#
# priority order, highest wins:
#   1) values passed directly:  Settings(log_level="DEBUG")
#   2) real environment variables
#   3) the .env file
#   4) default values written in the class
#
# SecretStr = a string that hides itself when printed or logged, so you cannot leak it by accident
# you must call .get_secret_value() on purpose when you really need the real text

class Settings(BaseSettings):
    # env_file = which file to read, extra="ignore" = do not crash on unrelated lines in .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # field names match env var names, but NOT case sensitive:
    # weather_api_key  <-  WEATHER_API_KEY
    weather_api_key: SecretStr                       # no default = REQUIRED
    request_timeout: float = Field(default=10.0, gt=0)   # converted from text, must be above 0
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    log_file: str | None = None                      # optional, None means no log file
    debug: bool = False

# get_settings() with lru_cache = build the settings only ONCE and reuse them everywhere
@lru_cache
def get_settings() -> Settings:
    return Settings()       # raises ValidationError right here if config is missing

# env_prefix option: model_config = SettingsConfigDict(env_prefix="WEATHERAPP_")
# then the variable names become WEATHERAPP_WEATHER_API_KEY, helpful to avoid name clashes


# PART 4: handling missing configuration (fail fast, fail clearly)
# rule: check config at STARTUP, not when the user clicks a button an hour later
# show a clear message, but never print the secret values themselves

def load_settings_or_exit() -> Settings:
    try:
        return get_settings()
    except ValidationError as e:
        print("Configuration problem, please fix your .env file:")
        for err in e.errors():
            field = ".".join(str(part) for part in err["loc"])
            print(f"  - {field}: {err['msg']}")     # we print the field name and reason only
        # (e.errors() can include the bad input value, so we deliberately do not print it)
        sys.exit(1)                                  # exit code 1 = the program failed


# PART 5: logging (replace print with this)
# why not print()?
#   - no timestamp, no importance level, no source, cannot be switched off or sent to a file
#   - logging lets you keep detail in a file and show only warnings on screen
#
# the 5 levels (low to high):
#   DEBUG     tiny details for developers          (very noisy)
#   INFO      normal events: "fetching weather"
#   WARNING   something odd but the program continues: "retrying"
#   ERROR     something failed: "API returned 401"
#   CRITICAL  the whole program may not continue
# if the logger level is INFO, then DEBUG messages are dropped
#
# a LOGGER = the object you call (logger.info(...)), named after the file with __name__
# a HANDLER = where the messages go (screen, file)
# a FORMATTER = how each line looks (time, level, text)

logger = logging.getLogger(__name__)    # always use this one line at the top of each file

# a formatter that hides secrets in the FINAL text, including tracebacks
# safety net only: the real protection is to never log secrets in the first place
class RedactingFormatter(logging.Formatter):
    def __init__(self, *args, secrets: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.secrets = [s for s in (secrets or []) if s]    # ignore empty strings

    def format(self, record: logging.LogRecord) -> str:
        text = super().format(record)                       # builds the full line (and traceback)
        for secret in self.secrets:
            text = text.replace(secret, "***")
        return text

def setup_logging(level: str = "INFO", log_file: str | None = None,
                  secrets: list[str] | None = None) -> None:
    # call this ONCE at program start, in main, never inside library code
    formatter = RedactingFormatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        secrets=secrets,
    )

    handlers: list[logging.Handler] = [logging.StreamHandler()]    # screen
    if log_file:
        # RotatingFileHandler = when the file reaches maxBytes it starts a new one
        # keeps the last 3 old files, so the log never fills your disk
        handlers.append(RotatingFileHandler(log_file, maxBytes=1_000_000,
                                            backupCount=3, encoding="utf-8"))

    for handler in handlers:
        handler.setFormatter(formatter)

    # force=True = replace any old logging setup, so calling it twice does not duplicate lines
    logging.basicConfig(level=level, handlers=handlers, force=True)

    # IMPORTANT: libraries log the FULL url of every request at INFO or DEBUG level
    # if your api key is in the url (?appid=KEY), the library would write your key into the log!
    # so turn those libraries down to WARNING
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

# logging tips
# 1) use %s style, not f-strings:   logger.info("city=%s", city)
#    python only builds the text if that level is actually enabled (faster)
# 2) logger.exception("message") inside an except block logs the error PLUS the full traceback
#    (same as logger.error("message", exc_info=True))
# 3) log WHAT happened and the useful ids (city, status code), not whole objects
# 4) log levels from config, so you can switch DEBUG on without editing code


# PART 6: never log secrets (and more places they hide)
# BAD:   logger.info(f"Calling API with key {api_key}")
# BAD:   logger.error(f"Request failed: {error}")     <- see the next lines!
# GOOD:  logger.info("Calling weather API for city=%s", city)
#
# sneaky leak 1: requests.exceptions.HTTPError text contains the FULL url, key included:
#   401 Client Error: Unauthorized for url: https://...weather?q=London&appid=YOUR_KEY
#   so logging str(error) or using logger.exception on it writes your key to the log file
#   fix: log only the status code, or use the redacting formatter above as a safety net
# sneaky leak 2: httpx / urllib3 debug logs print the url (handled in setup_logging above)
# sneaky leak 3: printing a whole settings or config object (SecretStr protects you here)
# sneaky leak 4: crash reports, screenshots, copy pasted terminal output, chat messages to AI tools
# sneaky leak 5: committing a .env, a notebook output, or a "test_key.txt" file


# PART 7: separate configuration from business logic
# business logic = what the program DOES (get weather, convert units)
# configuration  = the settings it needs (api key, timeout)
# bad:  the function reaches out and grabs a hard-coded key by itself
# good: the function RECEIVES the key as a parameter, and only main() reads the settings
# benefits: you can test it with a fake key (note 63), reuse it, and change settings without editing logic

URL = "https://api.openweathermap.org/data/2.5/weather"

class WeatherError(Exception):
    """our own error type, so callers catch ONE thing and never see raw library errors"""

def get_weather(city: str, api_key: str, timeout: float = 10.0) -> dict:
    # note: no settings, no os.environ in here, everything it needs comes in as arguments
    logger.info("Fetching weather for city=%s", city)
    try:
        # params= builds and URL-encodes the query for you (safer than an f-string url:
        # a city typed as "x&appid=other" cannot sneak extra parameters in)
        # timeout is required, without it requests can wait forever
        response = requests.get(URL, params={"q": city, "appid": api_key}, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        logger.error("Weather API returned status=%s for city=%s", status, city)  # status only, no url
        raise WeatherError(f"Weather API error {status}") from None    # from None hides the url-carrying chain
    except requests.exceptions.Timeout:
        logger.warning("Weather API timed out after %ss for city=%s", timeout, city)
        raise WeatherError("The request timed out") from None
    except requests.exceptions.RequestException as e:
        logger.error("Request failed (%s) for city=%s", type(e).__name__, city)   # type name only
        raise WeatherError("Could not reach the weather service") from None

    logger.debug("Weather API replied with %d bytes", len(response.content))
    return response.json()


# PART 8: wiring it together (this is the only place that reads settings)
def main() -> None:
    settings = load_settings_or_exit()                       # 1) config, stop early if broken
    setup_logging(                                           # 2) logging, using the config
        level=settings.log_level,
        log_file=settings.log_file,
        secrets=[settings.weather_api_key.get_secret_value()],
    )
    logger.info("App started (debug=%s)", settings.debug)    # 3) now run the real program
    try:
        data = get_weather("London", settings.weather_api_key.get_secret_value(),
                           settings.request_timeout)
        print(data["main"]["temp"])
    except WeatherError as e:
        print(f"Sorry: {e}")                                 # friendly message for the user,
                                                             # details are already in the log

# how to plug this into your PyQt5 Weather app (Project/20_WeatherAPIapp.py):
# 1) delete the hard-coded api_key line
# 2) at startup:   settings = load_settings_or_exit(); setup_logging(settings.log_level, ...)
# 3) inside get_weather(self):
#        api_key = settings.weather_api_key.get_secret_value()
#        response = requests.get(URL, params={"q": city, "appid": api_key}, timeout=settings.request_timeout)
# 4) keep your match/case error messages for the user, and add logger.error(...) beside each one
# note: your current requests.get(url) has NO timeout, so the "except Timeout" branch can basically
#       never trigger, always pass timeout=...


# PART 9: a leaked key checklist (what to do if a secret was committed)
# 1) REVOKE or ROTATE the key first, in the provider's dashboard, this is the real fix
#    (assume it is stolen the moment it is public, deleting the file does not un-leak it)
# 2) git keeps history forever, so removing the line in a new commit is NOT enough
#    search history for it:       git log -p -S "part_of_the_key"
# 3) remove it from ALL history with git filter-repo (or the BFG tool), then force push:
#        git filter-repo --replace-text replacements.txt
#        git push --force --all
#    (anyone who already cloned or forked still has the old copy, so step 1 matters most)
# 4) add the file to .gitignore and use env vars from now on
# 5) turn on GitHub secret scanning and push protection in the repo settings (free for public repos)
# 6) optional: a pre-commit scanner such as gitleaks blocks commits that contain secrets


# PART 10: more security habits for your future AI projects
# 1) least privilege: create keys with the smallest permissions they need
# 2) set spending limits and alerts on paid AI / cloud keys, a leaked LLM key can cost real money
# 3) separate keys for development and production, so leaking one does not hurt the other
# 4) never put secrets in frontend code, a mobile app, or a browser, anyone can read them
#    (the key must live on YOUR server, the frontend calls your server)
# 5) rotate keys on a schedule, and when a teammate leaves
# 6) validate every input you do not control with pydantic (note 61B)
# 7) never use eval() or exec() on user or LLM text, and never unpickle files you do not trust
# 8) use parameters, not string building: requests params=..., SQL placeholders (?), never f-string SQL
# 9) always use https:// urls, and do not turn off certificate checking (verify=False)
# 10) keep dependencies pinned (uv.lock) and updated, run "uv pip list --outdated" now and then
# 11) prompt injection: text from the web or users can contain instructions meant to trick an LLM,
#     treat LLM input AND output as untrusted data (you will study this in the AI track)
# SDKs read standard names automatically: OPENAI_API_KEY, ANTHROPIC_API_KEY, so just set them in .env


# PART 11: a runnable demo (no internet and no real key needed)
def demo() -> None:
    demo_env_vars()

    # missing required config -> clear error
    os.environ.pop("WEATHER_API_KEY", None)
    try:
        Settings(_env_file=None)             # _env_file=None = do not read any .env file now
    except ValidationError as e:
        print("missing config:", [err["loc"] for err in e.errors()])   # [('weather_api_key',)]

    # load from a temporary .env file (a stand-in for your real one)
    with tempfile.TemporaryDirectory() as folder:
        env_path = Path(folder) / ".env"
        env_path.write_text("WEATHER_API_KEY=fake-key-123\nLOG_LEVEL=DEBUG\nREQUEST_TIMEOUT=5\n")

        settings = Settings(_env_file=env_path)
        print(settings)
        # weather_api_key=SecretStr('**********') request_timeout=5.0 log_level='DEBUG' ...
        print(settings.request_timeout, type(settings.request_timeout))   # 5.0 <class 'float'>
        print(settings.weather_api_key.get_secret_value())                # fake-key-123 (on purpose)

        # real environment variables beat the .env file
        os.environ["LOG_LEVEL"] = "ERROR"
        print(Settings(_env_file=env_path).log_level)                     # ERROR
        del os.environ["LOG_LEVEL"]

        # logging with the secret hidden
        key = settings.weather_api_key.get_secret_value()
        setup_logging(level="DEBUG", secrets=[key])
        logger.debug("a tiny detail")
        logger.info("normal event")
        logger.warning("something odd")
        logger.error("accidentally leaked the key: %s", key)    # prints *** instead of the key
        try:
            1 / 0
        except ZeroDivisionError:
            logger.exception("caught an error")                 # message plus full traceback

    # a failing call is logged, and the user gets a clean message (no internet needed to see this)
    try:
        get_weather("London", "fake-key-123", timeout=3)
    except WeatherError as e:
        print("user sees:", e)

if __name__ == "__main__":
    demo()
    # for the real app, run main() instead (needs a real .env):  main()


# quick summary to remember
# os.getenv("X")                    -> read an env var (always a string)
# .env + .gitignore                 -> keep secrets out of git, commit only .env.example
# BaseSettings + SecretStr          -> typed, validated config that hides secrets when printed
# fail fast at startup              -> check config before doing real work
# logging.getLogger(__name__)       -> one logger per file
# logger.info("x=%s", x)            -> lazy formatting, use levels correctly
# logger.exception("msg")           -> error plus traceback (careful, tracebacks can contain urls)
# setup_logging() once in main      -> handlers, format, quiet down httpx and urllib3
# functions receive config as arguments -> easy to test, no hidden globals
# leaked key -> revoke first, then clean history, then prevent it happening again
