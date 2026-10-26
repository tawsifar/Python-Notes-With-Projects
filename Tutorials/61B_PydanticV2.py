# note: topics 61, 61B, 62, 63 and 64 were added later by me. the comments in these topics only were written by AI, and I reviewed them multiple times myself. I think they are good enough to explain everything clearly.

# pydantic = a library that CHECKS your data at runtime and converts it to the right types
# type hints alone do nothing at runtime, pydantic reads the hints and enforces them
# why it matters: data from APIs, files and users is not trustworthy
# (missing keys, wrong types, null values), pydantic catches problems early with a clear error
# install: uv add pydantic       (or: pip install pydantic)
# this note uses pydantic v2 (the current version)

from pydantic import (
    BaseModel, Field, ValidationError,
    field_validator, model_validator, ConfigDict,
)


# 1) BaseModel basics
# make a class that inherits BaseModel, write fields as hints
# pydantic builds __init__ and checks everything when you create an object
class User(BaseModel):
    name: str
    age: int
    email: str | None = None   # has a default, so it is optional

u = User(name="Tawsif", age=21)
print(u)          # name='Tawsif' age=21 email=None
print(u.name)     # Tawsif  (use dot access, not u["name"])

# pydantic converts (coerces) values when it safely can
u2 = User(name="Ali", age="25")   # "25" is a str, but it can become int 25
print(u2.age, type(u2.age))       # 25 <class 'int'>

# invalid data raises ValidationError (it does not fail silently)
try:
    User(name="Sara", age="abc")   # "abc" cannot become an int
except ValidationError as e:
    print(e)
    # 1 validation error for User
    # age
    #   Input should be a valid integer, unable to parse string as an integer ...

# missing required field is also an error
try:
    User(name="Sara")   # age is missing
except ValidationError as e:
    print(e.error_count(), "error")   # 1 error


# 2) reading errors in a clean way
# e.errors() gives a list of dicts, great for logging or showing the user
try:
    User(name=123, age="abc")
except ValidationError as e:
    for err in e.errors():
        # loc = which field, msg = what went wrong, type = short error code
        print(err["loc"], "->", err["msg"], f"({err['type']})")
    # ('name',) -> Input should be a valid string (string_type)
    # ('age',) -> Input should be a valid integer, unable to parse string as an integer (int_parsing)


# 3) strict mode = turn OFF the auto conversion
# strict=True means "25" will NOT become 25, it must already be an int
class StrictUser(BaseModel):
    model_config = ConfigDict(strict=True)
    name: str
    age: int

try:
    StrictUser(name="Ali", age="25")
except ValidationError as e:
    print("strict failed:", e.errors()[0]["msg"])   # Input should be a valid integer


# 4) Field() = add rules and extra info to a field
# gt/ge = greater than / greater or equal, lt/le = less than / less or equal
# min_length / max_length for strings and lists, pattern for regex
class Product(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)                       # must be more than 0
    quantity: int = Field(default=1, ge=1, le=100)   # between 1 and 100, default 1
    sku: str = Field(pattern=r"^[A-Z]{3}-\d{3}$")    # like ABC-123
    tags: list[str] = Field(default_factory=list)    # safe way to default to an empty list
    description: str = Field(default="", description="Short text about the product")

p = Product(name="Mouse", price=19.99, sku="ABC-123")
print(p)   # name='Mouse' price=19.99 quantity=1 sku='ABC-123' tags=[] description=''

try:
    Product(name="M", price=-5, sku="bad")
except ValidationError as e:
    print(e.error_count(), "errors")   # 3 errors (name too short, price not > 0, sku bad pattern)

# alias = the data uses one key name, your code uses another
# useful when the API key is not a nice python name (like "temp_min" vs "tempMin")
class Item(BaseModel):
    item_id: int = Field(alias="itemId")

item = Item(itemId=7)      # data comes in with the alias
print(item.item_id)        # 7  (you use the clean name in code)


# 5) nested models = a model inside another model
# this matches nested JSON perfectly, pydantic checks every level
class Address(BaseModel):
    city: str
    country: str

class Person(BaseModel):
    name: str
    address: Address              # nested model
    phones: list[str] = []        # list of strings (pydantic copies mutable defaults safely)

person = Person(name="Ali", address={"city": "Paris", "country": "France"})   # a dict is enough
print(person.address.city)   # Paris


# 6) validating a real API response (like your Weather app)
# openweathermap returns nested JSON, here is a shortened sample of it
api_response = {
    "cod": 200,
    "name": "London",
    "main": {"temp": 288.15, "humidity": 70},
    "weather": [{"id": 800, "description": "clear sky"}],
}

# describe the shape ONCE, as models
class Main(BaseModel):
    temp: float            # kelvin, because the API sends kelvin
    humidity: int

class Weather(BaseModel):
    id: int
    description: str

class WeatherResponse(BaseModel):
    cod: int
    name: str
    main: Main
    weather: list[Weather]

    # @property works on models too, handy for conversions
    @property
    def temp_celsius(self) -> float:
        return self.main.temp - 273.15

# model_validate = turn a dict into a validated model (this is the one to remember)
data = WeatherResponse.model_validate(api_response)
print(data.name)                       # London
print(data.weather[0].description)     # clear sky
print(f"{data.temp_celsius:.1f}")      # 15.0

# the OLD way (what your project does now):
#   data["main"]["temp"]  -> crashes with KeyError / TypeError if the API sends something unexpected
# the NEW way:
#   validate first, then use data.main.temp, bad data is rejected at the door with a clear error

# what happens when the API gives broken data
bad_response = {"cod": 200, "name": "London", "main": {"humidity": 70}, "weather": []}
try:
    WeatherResponse.model_validate(bad_response)
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])
    # ('main', 'temp') -> Field required

# unknown extra keys are IGNORED by default (the API can add fields without breaking you)
# to be strict about it use: model_config = ConfigDict(extra="forbid")


# 7) model_validate_json = validate a raw JSON STRING directly (skips json.loads)
json_text = '{"name": "Ali", "age": 30}'
u3 = User.model_validate_json(json_text)
print(u3)   # name='Ali' age=30 email=None
# with requests you can also do: Model.model_validate(response.json())


# 8) going back out: model to dict / JSON
print(u3.model_dump())          # {'name': 'Ali', 'age': 30, 'email': None}   (a python dict)
print(u3.model_dump_json())     # {"name":"Ali","age":30,"email":null}        (a JSON string)
print(u3.model_dump(exclude_none=True))   # {'name': 'Ali', 'age': 30}  (drops None values)
print(u3.model_dump(include={"name"}))    # {'name': 'Ali'}  (only chosen fields)
# note: in pydantic v1 these were .dict() and .json(), they are removed or deprecated in v2


# 9) field_validator = your own rule for ONE field
# runs after the normal type check by default
# must be a @classmethod, receives the value, returns the (maybe cleaned) value
class Signup(BaseModel):
    username: str
    password: str

    @field_validator("username")
    @classmethod
    def clean_username(cls, value: str) -> str:
        value = value.strip().lower()          # clean it
        if " " in value:
            raise ValueError("username cannot contain spaces")   # reject it
        return value                           # ALWAYS return the value

    @field_validator("password")
    @classmethod
    def strong_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("password must be at least 8 characters")
        if not any(ch.isdigit() for ch in value):
            raise ValueError("password must contain a number")
        return value

s = Signup(username="  AZIOM ", password="secret123")
print(s.username)   # aziom

try:
    Signup(username="a b", password="123")
except ValidationError as e:
    print(e.error_count(), "errors")   # 2 errors

# mode="before" runs BEFORE the type check, useful to fix messy input first
class Price(BaseModel):
    amount: float

    @field_validator("amount", mode="before")
    @classmethod
    def remove_dollar(cls, value):
        if isinstance(value, str):
            return value.replace("$", "").replace(",", "")   # "$1,200" -> "1200"
        return value

print(Price(amount="$1,200").amount)   # 1200.0


# 10) model_validator = a rule that compares MORE THAN ONE field
# mode="after" runs after all fields are valid, it receives the finished model (self)
class DateRange(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")
    def check_order(self):
        if self.end < self.start:
            raise ValueError("end must be after start")
        return self   # ALWAYS return self

try:
    DateRange(start=10, end=5)
except ValidationError as e:
    print(e.errors()[0]["msg"])   # Value error, end must be after start

class PasswordForm(BaseModel):
    password: str
    confirm: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm:
            raise ValueError("passwords do not match")
        return self


# 11) model_json_schema = get a JSON Schema that describes your model
# this is VERY important for AI work, because LLM structured output and
# function / tool calling use exactly this kind of schema
import json

print(json.dumps(User.model_json_schema(), indent=2))
# {
#   "properties": {
#     "name":  {"title": "Name", "type": "string"},
#     "age":   {"title": "Age", "type": "integer"},
#     "email": {"anyOf": [{"type": "string"}, {"type": "null"}], "default": null, "title": "Email"}
#   },
#   "required": ["name", "age"],
#   "title": "User",
#   "type": "object"
# }

# AI workflow you will use a lot:
# 1) define a BaseModel for the answer you want from the LLM
# 2) send model_json_schema() to the LLM as the required format
# 3) take the LLM's JSON reply and run Model.model_validate_json(reply)
# 4) if it raises ValidationError, retry or fix, you never use broken data


# 12) other handy things
# frozen = object cannot be changed after creation (like a constant)
class Point(BaseModel):
    model_config = ConfigDict(frozen=True)
    x: int
    y: int

pt = Point(x=1, y=2)
try:
    pt.x = 5
except ValidationError:
    print("cannot change a frozen model")

# validate_assignment = also check values when you change a field later
class Counter(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    count: int = 0

c = Counter()
c.count = "5"          # converted to int 5
print(c.count)         # 5

# model_copy = make a copy, optionally changing some fields
u4 = u3.model_copy(update={"age": 31})
print(u4.age)   # 31

# Literal and Enum work as fields too
from typing import Literal

class Task(BaseModel):
    title: str
    status: Literal["todo", "doing", "done"] = "todo"

Task(title="Study", status="doing")                 # fine
try:
    Task(title="Study", status="sleeping")          # not allowed
except ValidationError:
    print("invalid status")

# quick summary to remember
# class X(BaseModel): fields with hints        -> define the shape
# X(...) or X.model_validate(dict)             -> validate a dict
# X.model_validate_json(text)                  -> validate a JSON string
# x.model_dump() / x.model_dump_json()         -> back to dict / JSON
# Field(gt=0, min_length=2, alias=..., default_factory=list) -> extra rules
# @field_validator("field")   -> custom rule for one field (return the value)
# @model_validator(mode="after") -> rule across fields (return self)
# X.model_json_schema()       -> JSON Schema (used for LLM structured output)
# ValidationError + e.errors() -> read what went wrong
