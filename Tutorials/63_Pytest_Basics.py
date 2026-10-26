# note: topics 61, 61B, 62, 63 and 64 were added later by me. the comments in these topics only were written by AI, and I reviewed them multiple times myself. I think they are good enough to explain everything clearly.

# testing = writing code that checks your other code, so you find bugs BEFORE users do
# pytest = the most popular python testing tool, tests are just plain functions with assert
# uv = a very fast tool to manage python projects (packages, virtual env, python versions)
#
# how to run THIS note file:
#   uv run pytest 63_Pytest_Basics.py -v
#   (or without uv:  pip install pytest requests httpx  then  pytest 63_Pytest_Basics.py -v)
# every test below uses a FAKE network, so no internet and no real api key is needed


# PART A: uv basics (commands, run these in your terminal)
#
# uv init weather-project         -> creates a new project folder with pyproject.toml
# cd weather-project
# uv add requests httpx pydantic  -> installs packages AND records them in pyproject.toml
# uv add --dev pytest             -> installs a package only for development (testing tools)
# uv remove requests              -> uninstalls a package and updates pyproject.toml
# uv run python main.py           -> runs a script inside the project's virtual environment
# uv run pytest                   -> runs your tests inside the project's virtual environment
# uv sync                         -> installs everything the project needs (use after git clone)
# uv python install 3.12          -> installs a python version for you
#
# files uv creates:
#   pyproject.toml  = project info + list of dependencies (the file YOU edit or let uv edit)
#   uv.lock         = exact versions of every package, so everyone gets the same setup (commit it)
#   .venv/          = the virtual environment folder (do NOT commit it, put it in .gitignore)
#   .python-version = which python version the project uses
#
# why a virtual environment? each project gets its own packages,
# so project A can use pydantic v1 while project B uses pydantic v2 without fighting


# PART B: pytest rules you must remember
#
# 1) test files are named  test_something.py  (or something_test.py)
# 2) test functions start with  test_
# 3) test classes start with  Test  (and have no __init__)
# 4) a test PASSES if no exception is raised, it FAILS if an assert is false or any error happens
# 5) put tests in a  tests/  folder next to your code
#
# useful commands:
#   pytest                      run everything pytest can find
#   pytest -v                   verbose, shows every test name
#   pytest -x                   stop at the first failure
#   pytest -k "weather"         run only tests with "weather" in the name
#   pytest --lf                 run only the tests that failed last time
#   pytest -s                   show print() output (pytest hides it by default)
#   pytest file.py::test_name   run one specific test
#
# (this note file is named 63_..., so we pass the file name directly, pytest then runs it anyway)

import os
import asyncio
import pytest
import requests
import httpx


# PART C: the code we want to test
# normally this lives in its own file (like weather.py) and the test file imports it
# here it is in the same file so the note stays in one place

def load_api_key() -> str:
    key = os.getenv("WEATHER_API_KEY")        # reads from environment variables
    if not key:
        raise RuntimeError("WEATHER_API_KEY is not set")
    return key

def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15

def get_weather(city: str) -> dict:
    if not city.strip():
        raise ValueError("city cannot be empty")
    api_key = load_api_key()
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": api_key},
        timeout=10,
    )
    response.raise_for_status()               # 4xx / 5xx become an exception
    return response.json()

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


# PART D: your first tests with assert
# assert condition  -> test fails if the condition is False
# pytest shows both sides of the comparison when it fails, very helpful

def test_divide_normal():
    assert divide(10, 2) == 5

def test_kelvin_to_celsius():
    # floats are not exact in computers (0.1 + 0.2 is 0.30000000000000004)
    # so NEVER compare floats with ==, use pytest.approx
    assert kelvin_to_celsius(300) == pytest.approx(26.85)
    assert kelvin_to_celsius(273.15) == pytest.approx(0)

def test_basic_asserts():
    assert 5 > 3
    assert "a" in "cat"
    assert [1, 2, 3] == [1, 2, 3]
    assert {"a": 1}.get("b") is None
    assert not []                  # empty list is falsy


# PART E: testing that an error IS raised  (pytest.raises)
# the test passes only if that exact exception happens inside the with block
# match= checks the error message with a regex (part of the text is enough)

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError, match="cannot divide"):
        divide(1, 0)

def test_raises_gives_you_the_error_object():
    with pytest.raises(ValueError) as exc_info:
        get_weather("   ")                         # empty city, fails before any network call
    assert "city cannot be empty" in str(exc_info.value)


# PART F: parametrize = run ONE test with MANY inputs
# instead of copy pasting the same test 5 times
# each row becomes its own separate test in the report

@pytest.mark.parametrize(
    "a, b, expected",                # names of the arguments, as one string
    [
        (10, 2, 5),
        (9, 3, 3),
        (-6, 3, -2),
        (0, 5, 0),
        (1, 4, 0.25),
    ],
)
def test_divide_many_cases(a, b, expected):
    assert divide(a, b) == expected

# parametrize also works for error cases
@pytest.mark.parametrize("city", ["", "   ", "\n"])
def test_empty_city_is_rejected(city):
    with pytest.raises(ValueError):
        get_weather(city)

# ids= gives readable names to cases in the report
@pytest.mark.parametrize(
    "celsius, kelvin",
    [(0, 273.15), (100, 373.15), (-273.15, 0)],
    ids=["freezing", "boiling", "absolute-zero"],
)
def test_conversion_cases(celsius, kelvin):
    assert kelvin_to_celsius(kelvin) == pytest.approx(celsius)


# PART G: fixtures = reusable setup code
# a fixture is a function marked @pytest.fixture
# any test that has the fixture's NAME as a parameter automatically receives its value
# use fixtures for: sample data, fake objects, temporary files, setup and cleanup

@pytest.fixture
def sample_api_response() -> dict:
    # this is what a successful openweathermap reply looks like (shortened)
    return {
        "cod": 200,
        "name": "London",
        "main": {"temp": 288.15},
        "weather": [{"id": 800, "description": "clear sky"}],
    }

def test_sample_response_shape(sample_api_response):    # fixture name = parameter name
    assert sample_api_response["name"] == "London"

# fixture with cleanup: code after yield runs AFTER the test, even if the test failed
@pytest.fixture
def temp_numbers_file(tmp_path):
    # tmp_path is a BUILT IN fixture, a fresh empty temporary folder for each test
    file = tmp_path / "numbers.txt"
    file.write_text("1\n2\n3\n")
    yield file                                          # the test runs here
    print("cleanup runs here")                          # tmp_path is deleted by pytest anyway

def test_read_numbers(temp_numbers_file):
    numbers = [int(line) for line in temp_numbers_file.read_text().splitlines()]
    assert sum(numbers) == 6

# scope = how often the fixture is rebuilt
#   scope="function" (default) = new for every test
#   scope="module"   = once per file
#   scope="session"  = once for the whole run (good for expensive things like a database)
# fixtures shared by many files go in a file called conftest.py, pytest finds it automatically


# PART H: monkeypatch = temporarily change things during ONE test
# pytest puts everything back to normal after the test, you cannot forget to undo it
# main tools:
#   monkeypatch.setenv("NAME", "value")     set an environment variable
#   monkeypatch.delenv("NAME", raising=False)  remove an environment variable
#   monkeypatch.setattr(obj, "attr", new)   replace anything (function, method, variable)

# testing missing configuration (no api key at all)
def test_missing_api_key_raises(monkeypatch):
    monkeypatch.delenv("WEATHER_API_KEY", raising=False)   # make sure it is NOT set
    with pytest.raises(RuntimeError, match="WEATHER_API_KEY"):
        load_api_key()

def test_api_key_is_read_from_env(monkeypatch):
    monkeypatch.setenv("WEATHER_API_KEY", "fake-key-for-tests")   # never use a real key in tests
    assert load_api_key() == "fake-key-for-tests"

def test_empty_api_key_counts_as_missing(monkeypatch):
    monkeypatch.setenv("WEATHER_API_KEY", "")
    with pytest.raises(RuntimeError):
        load_api_key()


# PART I: mocking network calls (no internet needed)
# a unit test should never call a real api because real apis are slow,
# can be down, can cost money, and give different answers each time
# idea: replace requests.get with a fake function that returns whatever we want

class FakeResponse:
    # a tiny fake that has only what our code uses
    def __init__(self, status_code: int = 200, json_data: dict | None = None):
        self.status_code = status_code
        self._json_data = json_data or {}

    def json(self) -> dict:
        return self._json_data

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f"{self.status_code} error")

@pytest.fixture
def fake_key(monkeypatch):
    monkeypatch.setenv("WEATHER_API_KEY", "fake-key-for-tests")

def test_get_weather_success(monkeypatch, fake_key, sample_api_response):
    def fake_get(url, params=None, timeout=None):       # same shape as requests.get
        return FakeResponse(200, sample_api_response)

    # IMPORTANT: patch the name where it is LOOKED UP
    # our code calls requests.get(...), so we replace the "get" attribute on the requests module
    monkeypatch.setattr(requests, "get", fake_get)

    result = get_weather("London")
    assert result["name"] == "London"
    assert result["weather"][0]["description"] == "clear sky"

# you can also check HOW the function was called by recording the arguments
def test_get_weather_sends_city_and_key(monkeypatch, fake_key, sample_api_response):
    captured = {}                                        # a dict that remembers the call

    def fake_get(url, params=None, timeout=None):
        captured["url"] = url
        captured["params"] = params
        captured["timeout"] = timeout
        return FakeResponse(200, sample_api_response)

    monkeypatch.setattr(requests, "get", fake_get)
    get_weather("Paris")

    assert captured["params"]["q"] == "Paris"
    assert captured["params"]["appid"] == "fake-key-for-tests"
    assert captured["timeout"] is not None               # we never want a request without a timeout

# failure cases are the most valuable tests (what happens when the API breaks?)
@pytest.mark.parametrize("status", [401, 404, 500])
def test_get_weather_http_errors(monkeypatch, fake_key, status):
    monkeypatch.setattr(requests, "get", lambda *a, **k: FakeResponse(status))
    with pytest.raises(requests.exceptions.HTTPError):
        get_weather("London")

def test_get_weather_timeout(monkeypatch, fake_key):
    def fake_get(*args, **kwargs):
        raise requests.exceptions.Timeout("too slow")    # pretend the server never answered
    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(requests.exceptions.Timeout):
        get_weather("London")

def test_get_weather_connection_error(monkeypatch, fake_key):
    def fake_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError("no internet")
    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(requests.exceptions.ConnectionError):
        get_weather("London")

def test_get_weather_without_key_never_calls_network(monkeypatch):
    monkeypatch.delenv("WEATHER_API_KEY", raising=False)
    def fake_get(*args, **kwargs):
        pytest.fail("network must not be called when the key is missing")
    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(RuntimeError):
        get_weather("London")


# PART J: unittest.mock (the standard library alternative to monkeypatch)
# patch("requests.get") replaces requests.get inside the with block
# MagicMock accepts any call and records it, so you can ask "was it called? with what?"
from unittest.mock import MagicMock, patch

def test_with_magicmock(fake_key, sample_api_response):
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: sample_api_response,            # json() returns our dict
        )
        result = get_weather("Tokyo")

    assert result["name"] == "London"                    # our fake data, whatever the city
    mock_get.assert_called_once()                        # called exactly one time
    assert mock_get.call_args.kwargs["params"]["q"] == "Tokyo"   # check the arguments used

# monkeypatch vs mock, which one?
# monkeypatch = simple replace of one thing, very readable (good default)
# mock / patch = when you want to inspect calls (assert_called_with) or need side_effect lists


# PART K: testing async code (note 62)
# simplest way, no plugin: run the coroutine inside the test with asyncio.run
# httpx.MockTransport = a fake network for httpx, you give it a function that builds the reply
# the plugin way: uv add --dev pytest-asyncio, then mark the test with @pytest.mark.asyncio and use async def

async def fetch_temp(client: httpx.AsyncClient, lat: float, lon: float) -> float:
    response = await client.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m"},
    )
    response.raise_for_status()
    return response.json()["current"]["temperature_2m"]

def test_async_fetch_temp_success():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"current": {"temperature_2m": 21.5}})

    async def scenario():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            return await fetch_temp(client, 51.5, -0.12)

    assert asyncio.run(scenario()) == 21.5

def test_async_fetch_temp_server_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(503)                       # pretend the server is down

    async def scenario():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            await fetch_temp(client, 51.5, -0.12)

    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(scenario())

def test_async_concurrent_calls_all_return():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"current": {"temperature_2m": 10.0}})

    async def scenario():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            return await asyncio.gather(*[fetch_temp(client, 0, i) for i in range(5)])

    assert asyncio.run(scenario()) == [10.0] * 5


# PART L: other handy built in features

# capsys = capture what the code printed
def say_hi(name: str) -> None:
    print(f"Hi {name}")

def test_print_output(capsys):
    say_hi("Tawsif")
    captured = capsys.readouterr()
    assert captured.out == "Hi Tawsif\n"

# skip = never run this test (with a reason)
@pytest.mark.skip(reason="feature not built yet")
def test_future_feature():
    assert False

# skipif = skip only under a condition
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="linux and mac only")
def test_unix_only():
    assert os.sep == "/"

# xfail = we KNOW this fails today (a known bug), do not turn the whole run red
@pytest.mark.xfail(reason="known bug, rounding not handled yet")
def test_known_bug():
    assert round(2.5) == 3        # python rounds 2.5 to 2 (banker's rounding), so this fails

# grouping tests in a class (optional, just for organisation)
class TestDivide:
    def test_positive(self):
        assert divide(8, 2) == 4

    def test_negative(self):
        assert divide(-8, 2) == -4


# PART M: good testing habits
# 1) one test checks one idea, name it like a sentence: test_missing_key_raises_error
# 2) test the failure paths too (timeouts, 404, bad input), not just the happy path
# 3) never call the real internet or use real secrets in unit tests
# 4) tests must not depend on each other or on their order
# 5) arrange, act, assert: set things up, call the code, check the result
# 6) if a bug is found, first write a test that fails because of it, then fix the code
# 7) run pytest before every git commit

# optional config in pyproject.toml so you do not type options every time
# [tool.pytest.ini_options]
# testpaths = ["tests"]
# addopts = "-v"

# quick summary to remember
# def test_x(): assert ...                 -> a test
# pytest.approx(x)                         -> compare floats
# with pytest.raises(Err, match="..."):    -> expect an error
# @pytest.mark.parametrize("a,b", [...])   -> many inputs, one test
# @pytest.fixture + yield                  -> reusable setup and cleanup
# monkeypatch.setenv / delenv / setattr    -> change env or replace functions for one test
# httpx.MockTransport                      -> fake network for async httpx
# tmp_path, capsys                         -> built in fixtures for files and printed output
# uv init / add / add --dev / run / sync   -> project and package management

if __name__ == "__main__":
    # lets you run this note file with plain "python 63_Pytest_Basics.py"
    raise SystemExit(pytest.main([__file__, "-v"]))
