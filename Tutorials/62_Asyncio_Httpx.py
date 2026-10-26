# note: topics 61, 61B, 62, 63 and 64 were added later by me. the comments in these topics only were written by AI, and I reviewed them multiple times myself. I think they are good enough to explain everything clearly.

# asyncio = python's way to run many WAITING tasks at the same time using ONE thread
# best for I/O bound work: API calls, database calls, downloads, anything that waits
# NOT for heavy calculations (CPU bound), for those use multiprocessing
# difference from threading (note 49): no extra threads, tasks politely take turns
# a task gives control back ONLY when it hits an "await"
# httpx = a modern HTTP library, like requests, but it also has an async version
# install: uv add httpx       (or: pip install httpx)
# needs python 3.10+ (a few parts below mention 3.11+)

import asyncio
import time
import httpx
from pydantic import BaseModel, ValidationError


# 1) the basics: async def, await, asyncio.run
# async def = makes a COROUTINE function (a function that can pause and resume)
# calling it does NOT run it, it only creates a coroutine object
# await = "pause me here until this finishes, and let other tasks run meanwhile"
# you can only use await INSIDE an async def
# asyncio.run(...) = starts the event loop and runs your main coroutine (call it once, at the bottom)

async def say_after(delay: float, message: str) -> str:
    await asyncio.sleep(delay)   # NON-blocking sleep, other tasks can run while this waits
    print(message)
    return message

async def demo_basics() -> None:
    coro = say_after(1, "hello")
    print(coro)        # <coroutine object say_after at 0x...>   (nothing has run yet!)
    result = await coro            # now it actually runs
    print("returned:", result)     # returned: hello

    # common beginner mistake: forgetting await
    # say_after(1, "oops")   # python only warns "coroutine was never awaited", nothing runs


# 2) sequential vs concurrent
# awaiting one after another = SEQUENTIAL (total time is the sum)
# asyncio.gather(...) = run them TOGETHER (total time is about the longest one)
async def demo_sequential_vs_gather() -> None:
    start = time.perf_counter()
    await say_after(1, "one")
    await say_after(1, "two")
    await say_after(1, "three")
    print(f"sequential: {time.perf_counter() - start:.2f}s")   # about 3.00s

    start = time.perf_counter()
    results = await asyncio.gather(
        say_after(1, "one"),
        say_after(1, "two"),
        say_after(1, "three"),
    )
    print(f"gather: {time.perf_counter() - start:.2f}s")       # about 1.00s
    print(results)   # ['one', 'two', 'three']  (results come back in the SAME order you passed them)


# 3) create_task = start a coroutine in the background right now
# gather is nice for a fixed group, create_task is nice when you want to start something
# and keep doing other work, then await the result later
async def demo_create_task() -> None:
    task = asyncio.create_task(say_after(1, "background job done"))
    print("main keeps working while the task runs")
    await asyncio.sleep(0.2)
    print("still working...")
    await task   # wait for it to finish (important, do not forget it)
    # tip: keep a reference to the task (the variable "task"), otherwise python may delete it early


# 4) the #1 async mistake: blocking calls
# time.sleep(), requests.get(), and heavy loops BLOCK the whole event loop
# while they run, NO other task can run, so async gives you zero benefit
async def bad_example() -> None:
    time.sleep(1)            # BAD: freezes everything for 1 second
    # await asyncio.sleep(1) # GOOD: only this task waits

# rule: inside async def, use async libraries (httpx.AsyncClient, not requests)
# if you must call blocking code, push it to a thread:
async def demo_to_thread() -> None:
    result = await asyncio.to_thread(time.sleep, 1)   # runs in a worker thread, loop stays free
    print("blocking code finished in a thread")


# 5) httpx basics (sync version first, it feels just like requests)
# httpx.get(url) works like requests.get(url)
def demo_httpx_sync() -> None:
    response = httpx.get("https://api.open-meteo.com/v1/forecast",
                         params={"latitude": 51.5, "longitude": -0.12, "current": "temperature_2m"})
    print(response.status_code)   # 200
    print(response.json())
    # params={...} builds the ?key=value part for you, safely encoded
    # always prefer params over typing the query string into the url yourself


# 6) the weather example (open-meteo is free and needs NO api key)
# we want the current temperature for many cities
CITIES: dict[str, tuple[float, float]] = {
    "London": (51.51, -0.13),
    "Tokyo": (35.68, 139.69),
    "Paris": (48.85, 2.35),
    "New York": (40.71, -74.01),
    "Sydney": (-33.87, 151.21),
}

URL = "https://api.open-meteo.com/v1/forecast"

# a pydantic model checks the part of the response we need (note 61B)
class Current(BaseModel):
    temperature_2m: float
    wind_speed_10m: float

class CityWeather(BaseModel):
    city: str
    temperature: float
    wind: float

# the client is passed IN as a parameter, not created inside
# why: (1) one client can be reused for many requests (fast)
#      (2) tests can pass a fake client (note 63)
async def fetch_weather(client: httpx.AsyncClient, city: str) -> CityWeather:
    lat, lon = CITIES[city]
    response = await client.get(URL, params={
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    })
    response.raise_for_status()   # raises httpx.HTTPStatusError for 4xx / 5xx (like requests)
    current = Current.model_validate(response.json()["current"])   # validate before using
    return CityWeather(city=city, temperature=current.temperature_2m, wind=current.wind_speed_10m)


# 7) AsyncClient and timeouts
# "async with" opens the client and closes it properly at the end (like "with open(...)")
# REUSE one client for many requests, it keeps connections open, creating a new client
# for every request is slow and wasteful
#
# timeouts: httpx has a default of 5 seconds, never wait forever in real programs
# httpx.Timeout(10.0, connect=3.0) = 10s for everything, but only 3s to connect
# parts: connect (open connection), read (waiting for data), write, pool (waiting for a free connection)
timeout = httpx.Timeout(10.0, connect=3.0)

async def demo_one_request() -> None:
    async with httpx.AsyncClient(timeout=timeout) as client:
        weather = await fetch_weather(client, "London")
        print(weather)   # city='London' temperature=11.4 wind=9.2   (your numbers will differ)


# 8) HTTP status and exception handling
# httpx.HTTPStatusError  = server answered with 4xx / 5xx (only raised by raise_for_status())
# httpx.TimeoutException = took too long (ConnectTimeout, ReadTimeout, ...)
# httpx.ConnectError     = could not connect (no internet, wrong host)
# httpx.RequestError     = parent of timeout / connect errors (anything that failed while sending)
# httpx.HTTPError        = parent of EVERYTHING above
# order matters: put the specific ones first, the general one last (same rule as note 44)
async def safe_fetch(client: httpx.AsyncClient, city: str) -> CityWeather | None:
    try:
        return await fetch_weather(client, city)
    except httpx.HTTPStatusError as e:
        print(f"{city}: server said {e.response.status_code}")   # e.response has the full response
    except httpx.TimeoutException:
        print(f"{city}: request timed out")
    except httpx.ConnectError:
        print(f"{city}: could not connect, check internet")
    except httpx.RequestError as e:
        print(f"{city}: request failed ({type(e).__name__})")
    except ValidationError:
        print(f"{city}: API sent data in an unexpected shape")   # pydantic caught bad data
    return None   # explicit None so the caller knows it failed

# status codes you will meet again and again
# 400 bad request, 401 bad / missing api key, 403 forbidden, 404 not found,
# 429 too many requests (slow down!), 500 / 502 / 503 / 504 = server side problems


# 9) the main task: five cities, sequential vs concurrent
# measure both and compare, do NOT assume a fixed speedup
# the speedup depends on your internet, the server, and rate limits
async def demo_compare_speed() -> None:
    async with httpx.AsyncClient(timeout=timeout) as client:

        start = time.perf_counter()
        sequential = []
        for city in CITIES:
            sequential.append(await safe_fetch(client, city))   # one at a time
        t_seq = time.perf_counter() - start

        start = time.perf_counter()
        # list comprehension makes the list of coroutines, * unpacks them into gather's arguments
        concurrent = await asyncio.gather(*[safe_fetch(client, city) for city in CITIES])
        t_con = time.perf_counter() - start

        print(f"sequential: {t_seq:.2f}s")
        print(f"concurrent: {t_con:.2f}s")
        for item in concurrent:
            if item:
                print(f"{item.city}: {item.temperature}C, wind {item.wind} km/h")


# 10) gather and errors
# default: if ONE task raises, gather raises that error right away
# (the other tasks are NOT cancelled, they keep running in the background, which can surprise you)
# return_exceptions=True = errors are returned as values in the result list, nothing is raised
# you then check each result yourself
async def demo_return_exceptions() -> None:
    async with httpx.AsyncClient(timeout=timeout) as client:
        results = await asyncio.gather(
            *[fetch_weather(client, city) for city in CITIES],
            return_exceptions=True,
        )
        for city, result in zip(CITIES, results):
            if isinstance(result, Exception):          # this city failed
                print(f"{city} failed: {type(result).__name__}")
            else:                                      # this city worked
                print(f"{city}: {result.temperature}C")


# 11) limit how many run at once with a Semaphore
# firing 500 requests together can get you blocked (429) or overload your machine
# Semaphore(3) = at most 3 tasks may be inside the "async with sem" block at the same time
async def limited_fetch(sem: asyncio.Semaphore, client: httpx.AsyncClient, city: str) -> CityWeather | None:
    async with sem:                       # waits here if 3 tasks are already inside
        return await safe_fetch(client, city)

async def demo_semaphore() -> None:
    sem = asyncio.Semaphore(3)
    async with httpx.AsyncClient(timeout=timeout) as client:
        results = await asyncio.gather(*[limited_fetch(sem, client, c) for c in CITIES])
        print(len([r for r in results if r]), "cities fetched")


# 12) retry with backoff (simple version)
# network calls fail sometimes for no reason, retrying a few times often fixes it
# backoff = wait longer after each failure (1s, 2s, 4s) so you do not hammer the server
# only retry errors that can be temporary (timeouts, connection errors, 5xx), NOT 400 / 401 / 404
async def fetch_with_retry(client: httpx.AsyncClient, city: str, retries: int = 3) -> CityWeather:
    for attempt in range(1, retries + 1):
        try:
            return await fetch_weather(client, city)
        except (httpx.TimeoutException, httpx.ConnectError):
            pass                                    # temporary problem, try again
        except httpx.HTTPStatusError as e:
            if e.response.status_code < 500:        # 4xx = our fault, retrying will not help
                raise
        if attempt == retries:
            raise RuntimeError(f"{city}: failed after {retries} attempts")
        wait = 2 ** (attempt - 1)                   # 1, 2, 4 ...
        print(f"{city}: attempt {attempt} failed, retrying in {wait}s")
        await asyncio.sleep(wait)
    raise RuntimeError("unreachable")               # keeps type checkers happy
# in real projects the "tenacity" library does this for you with one decorator


# 13) overall timeout for a whole task: asyncio.wait_for
# the httpx timeout limits ONE request, wait_for limits the WHOLE coroutine
async def demo_wait_for() -> None:
    try:
        await asyncio.wait_for(asyncio.sleep(5), timeout=1)   # sleep is too slow
    except asyncio.TimeoutError:
        print("took longer than 1 second, cancelled")
    # python 3.11+ also has:  async with asyncio.timeout(1): ...


# 14) TaskGroup (python 3.11+) = the newer, safer alternative to gather
# if one task fails, the others are cancelled automatically, nothing is left running
async def demo_taskgroup() -> None:
    async with httpx.AsyncClient(timeout=timeout) as client:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch_weather(client, city)) for city in CITIES]
        # the block above only finishes when ALL tasks are done
        for t in tasks:
            print(t.result().city, t.result().temperature)
    # if any task raised, you get an ExceptionGroup, catch it with:  except* httpx.HTTPError


# 15) how to run things
# create ONE main coroutine, call it with asyncio.run() exactly once at the bottom
# do NOT call asyncio.run() inside an async function, and do NOT use await at top level of a script
# (in jupyter notebooks you CAN use top-level await, that is the one exception)
async def main() -> None:
    await demo_basics()
    await demo_sequential_vs_gather()
    await demo_create_task()
    await demo_to_thread()
    await demo_one_request()
    await demo_compare_speed()
    await demo_return_exceptions()
    await demo_semaphore()
    await demo_wait_for()
    await demo_taskgroup()

if __name__ == "__main__":
    asyncio.run(main())    # needs internet for the httpx demos


# extra notes
# 1) async is contagious: if function A awaits B, then A must be async too, all the way up to main
# 2) PyQt5 (your Weather app) has its own event loop, so asyncio.run() does not mix with it directly
#    simple options: run the request in a QThread, or use the "qasync" library
# 3) FastAPI (the usual next step for AI backends) is built on async def, so this note is the foundation
# 4) requests is blocking, so in async code use httpx.AsyncClient (or aiohttp)

# quick summary to remember
# async def f(): ...                      -> coroutine function
# await f()                               -> run it and wait for the result
# asyncio.run(main())                     -> start everything (once)
# await asyncio.gather(a(), b(), c())     -> run together, results keep their order
# asyncio.gather(..., return_exceptions=True) -> collect errors instead of raising
# asyncio.create_task(f())                -> start in background
# asyncio.Semaphore(n)                    -> limit concurrency
# async with httpx.AsyncClient(timeout=...) as client -> reuse one client, always set a timeout
# response.raise_for_status()             -> turn 4xx / 5xx into HTTPStatusError
# never use time.sleep() or requests inside async def
