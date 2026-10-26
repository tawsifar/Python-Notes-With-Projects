# note: topics 61, 61B, 62, 63 and 64 were added later by me. the comments in these topics only were written by AI, and I reviewed them multiple times myself. I think they are good enough to explain everything clearly.

# type hints = labels that tell humans and tools what type a value should be
# example: "this function takes a str and gives back an int"
# IMPORTANT: python does NOT enforce them when the program runs
# they are for: readability, editor autocomplete, and checkers like mypy / pyright
# pydantic (next note) is the library that actually enforces types at runtime
# needs python 3.10+ for the modern syntax used here (list[str], int | None)

# variable annotations
# syntax = name: type = value
name: str = "Tawsif"
age: int = 21
height: float = 5.9
is_student: bool = True

# python will NOT stop you from breaking the hint, it just runs
age = "twenty one"   # a checker like mypy would warn here, python itself does not care
print(age)           # twenty one

# you can write the hint first and assign later
score: int
score = 90


# function annotations
# params: name: type
# return type: -> type   (placed after the closing bracket)
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))   # 5

# -> None means the function returns nothing (like print)
def say_hello(name: str) -> None:
    print(f"Hello {name}")

say_hello("Tawsif")   # Hello Tawsif

# default values still work with hints
def greet(name: str, excited: bool = False) -> str:
    if excited:
        return f"Hello {name}!!!"
    return f"Hello {name}"

print(greet("Tawsif", excited=True))   # Hello Tawsif!!!


# collections
# old way (python 3.8 and before) needed: from typing import List, Dict
# new way (3.9+) = use the built-in names directly, so just write list[...] dict[...]
names: list[str] = ["Ali", "Sara", "Rahim"]        # list of strings
marks: dict[str, int] = {"math": 90, "cse": 95}    # keys are str, values are int
unique_ids: set[int] = {1, 2, 3}                    # set of ints
point: tuple[int, int] = (10, 20)                   # tuple with exactly 2 ints
rgb: tuple[int, int, int] = (255, 0, 0)             # exactly 3 ints
numbers: tuple[int, ...] = (1, 2, 3, 4, 5)          # ... means any length, all ints

# nested types work too
matrix: list[list[int]] = [[1, 2], [3, 4]]
students: dict[str, list[int]] = {"Ali": [80, 90], "Sara": [95, 85]}

def average(values: list[int]) -> float:
    return sum(values) / len(values)

print(average([80, 90, 100]))   # 90.0


# optional values (a value that can also be None)
# int | None means "an int OR None"   (3.10+ syntax)
# older way: Optional[int] from typing, it means exactly the same thing
from typing import Optional

def find_user(user_id: int) -> str | None:
    users = {1: "Ali", 2: "Sara"}
    return users.get(user_id)   # .get() gives None when the key is missing

user = find_user(5)
# a checker will warn if you use user.upper() directly, because it might be None
# so always check first
if user is not None:
    print(user.upper())
else:
    print("User not found")   # User not found

# Optional[str] is the older way to write str | None
def old_style(x: Optional[str] = None) -> Optional[str]:
    return x

# IMPORTANT: Optional does NOT mean "this argument is optional to pass"
# it only means the value may be None
# to make an argument optional to pass, you need a default value (= None)


# union (more than one allowed type)
# int | str means "an int OR a str"
# older way: Union[int, str] from typing
from typing import Union

def show_id(user_id: int | str) -> str:
    return f"ID is {user_id}"

print(show_id(101))        # ID is 101
print(show_id("A-101"))    # ID is A-101

def old_union(x: Union[int, float]) -> Union[int, float]:
    return x * 2

# isinstance narrowing = check the type, and the checker knows the type inside the if
def double(x: int | str) -> int | str:
    if isinstance(x, int):
        return x * 2        # checker knows x is int here
    return x + x            # checker knows x is str here

print(double(4))      # 8
print(double("ab"))   # abab


# Any = turn off checking for this value (use rarely, it defeats the purpose)
from typing import Any

def log_anything(value: Any) -> None:
    print(value)

# for real "anything" prefer object, or be specific if you can


# Literal = only these exact values are allowed
# great for modes, statuses, options
from typing import Literal

def set_mode(mode: Literal["light", "dark"]) -> None:
    print(f"Mode set to {mode}")

set_mode("dark")      # fine
# set_mode("blue")    # checker error, "blue" is not allowed (python still runs it though)

Status = Literal["pending", "done", "failed"]   # reusable name for a literal

def update_status(status: Status) -> None:
    print(f"Status: {status}")

update_status("done")   # Status: done


# type alias = give a long type a short readable name
Coordinates = tuple[float, float]
Scores = dict[str, list[int]]

def distance_from_origin(point: Coordinates) -> float:
    x, y = point
    return (x ** 2 + y ** 2) ** 0.5

print(distance_from_origin((3.0, 4.0)))   # 5.0


# Callable = a type for functions you pass around
# Callable[[arg types], return type]
from typing import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(apply(add, 4, 5))                   # 9
print(apply(lambda x, y: x * y, 4, 5))    # 20


# TypedDict = a dictionary with a fixed shape (known keys, known value types)
# very useful for JSON from an API
# it is only a hint, at runtime it is still a normal dict (no validation)
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

movie: Movie = {"title": "Inception", "year": 2010, "rating": 8.8}
print(movie["title"])   # Inception
# a checker would warn if you forget a key or use the wrong value type

# total=False makes ALL keys optional
class Profile(TypedDict, total=False):
    username: str
    bio: str

p: Profile = {"username": "azim"}   # bio is missing but that is fine
print(p)   # {'username': 'azim'}
# python 3.11+ also has NotRequired[...] to mark just one key as optional

# TypedDict vs pydantic BaseModel:
# TypedDict    = hint only, no checking, stays a dict
# BaseModel    = real checking at runtime, becomes an object
# for API data you do not trust, use pydantic (next note)


# dataclass + type hints
# dataclass writes __init__, __repr__, __eq__ for you from the annotations
# the hints here are required, the dataclass uses them to find the fields
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int
    grades: list[int] = field(default_factory=list)   # never use grades = [] directly
                                                      # a plain [] would be shared by all objects

s = Student("Ali", 20)
s.grades.append(90)
print(s)   # Student(name='Ali', age=20, grades=[90])


# hints on class methods and attributes
class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def get_balance(self) -> float:
        return self.balance

    # method that returns the same class: use quotes (a "forward reference")
    # because the class Account does not fully exist yet while python reads this line
    def copy(self) -> "Account":
        return Account(self.owner, self.balance)

acc = Account("Tawsif", 100.0)
acc.deposit(50)
print(acc.get_balance())   # 150.0
# python 3.11+ also has: from typing import Self, then -> Self


# TypeVar = generics, "whatever type goes in is the type that comes out"
# use when one function works for many types but input and output types are linked
from typing import TypeVar

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    return items[0]

print(first_item([1, 2, 3]))        # 1  (checker knows this is an int)
print(first_item(["a", "b", "c"]))  # a  (checker knows this is a str)
# python 3.12+ has a shorter syntax: def first_item[T](items: list[T]) -> T


# Final = a value that should never be changed (constants)
from typing import Final

MAX_RETRIES: Final = 3
# MAX_RETRIES = 5   # checker error (python still runs it, final is just a hint)


# generators and iterables
from typing import Iterable, Iterator, Generator

def total(numbers: Iterable[int]) -> int:   # accepts a list, tuple, set, generator...
    return sum(numbers)

print(total([1, 2, 3]))      # 6
print(total((4, 5, 6)))      # 15

# generator function = Generator[yield type, send type, return type]
# for simple cases use Iterator[yield type]
def count_up(limit: int) -> Iterator[int]:
    for i in range(limit):
        yield i

print(list(count_up(3)))   # [0, 1, 2]


# *args and **kwargs
# the hint describes ONE element, not the whole tuple or dict
def sum_all(*args: int) -> int:           # args is really tuple[int, ...]
    return sum(args)

def show_info(**kwargs: str) -> None:     # kwargs is really dict[str, str]
    print(kwargs)

print(sum_all(1, 2, 3))            # 6
show_info(name="Ali", city="London")   # {'name': 'Ali', 'city': 'London'}


# how to actually CHECK your hints
# 1) install a checker:   uv add --dev mypy       (or: pip install mypy)
# 2) run it:              mypy 61_TypeHints.py
# it reads your hints and prints errors WITHOUT running the code
# pyright is another popular checker (VS Code Pylance uses it)
# 3) you can see stored hints at runtime too
print(add.__annotations__)   # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

# quick summary to remember
# x: int                 -> variable hint
# def f(a: int) -> str   -> parameter and return hint
# list[str] dict[str,int]-> collections
# int | None             -> value or None
# int | str              -> either type
# Literal["a", "b"]      -> only these values
# TypedDict              -> dict with fixed keys (hint only)
# Callable[[int], str]   -> function type
# TypeVar                -> generics
# remember: hints are NOT enforced at runtime, use pydantic for that
