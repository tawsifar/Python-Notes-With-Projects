# dictionary = collection of key:value pairs
# ordered, changeable, no duplicate keys
# keys can be any immutable type: string, int, tuple

capitals = {"USA":    "Washington D.C.",
            "India":  "New Delhi",
            "China":  "Beijing",
            "Russia": "Moscow",
            404:      "Tawsif's Custom Capital XD"}  # int as key, totally valid

# accessing values
print(capitals["USA"])          # Washington D.C. - direct access, KeyError if not found
print(capitals.get("India"))    # New Delhi - safe access, returns None if not found
print(capitals.get("Japan"))    # None - no error, just None
print(capitals.get("Japan", "Not Found"))  # Not Found - custom default if key missing

# checking if key exists
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# safer way to check
print("Japan" in capitals)      # False
print("USA" in capitals)        # True

# adding and updating
capitals.update({"Japan": "Tokyo"})   # adds new key
capitals.update({"USA": "Ohio"})      # updates existing key

# removing
capitals.pop("China")       # removes specific key
capitals.popitem()          # removes last inserted item
# capitals.clear()          # removes everything

print(capitals)

# keys, values, items
for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

for key, value in capitals.items():   # most common way to loop a dictionary
    print(f"{key}: {value}")

# nested dictionary - Tawsif's student profile
student = {
    "name":   "Tawsif",
    "uni":    "CUET",
    "dept":   "CSE",
    "grades": {"math": 90, "physics": 85, "programming": 98}
}

print(student["name"])                  # Tawsif
print(student["grades"]["programming"]) # 98 - access nested value

# basic CP usage (optional)
# find frequency:
'''
#find frequency


from collections import defaultdict

arr = [1, 2, 3, 2, 1, 1, 3, 4]

freq = defaultdict(int)  # any missing key automatically starts at 0
for x in arr:
    freq[x] += 1         # no KeyError even if x was never seen before

print(dict(freq))   # {1: 3, 2: 2, 3: 2, 4: 1}



'''