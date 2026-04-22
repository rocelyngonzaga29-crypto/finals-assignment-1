# ===== LIST =====
# Lists are ordered, mutable, and allow duplicate members.
print("LIST:")
my_list = [3, 1, 5]

# Add 1 new item
my_list.append(2)

# Remove 1 item
my_list.remove(1)

# Sort the list
my_list.sort()

print("Updated List:", my_list)

# ===== TUPLE =====
# Tuples are ordered and immutable (cannot be changed).
print("\nTUPLE:")
my_tuple = (10, 20, 30)

# Try modifying one element to demonstrate immutability
try:
    my_tuple[0] = 100
except TypeError:
    print("Error: Tuple is immutable (hindi pwedeng baguhin)")

print("Tuple:", my_tuple)

# ===== SET =====
# Sets are unordered, unindexed, and do not allow duplicate members.
print("\nSET:")
my_set = {1, 2, 3}

# Add a value
my_set.add(4)

# Remove a value
my_set.remove(2)

# Print updated set
print("Updated Set:", my_set)

# ===== DICTIONARY =====
# Dictionaries are ordered (as of Python 3.7) and changeable. No duplicate keys.
print("\nDICTIONARY:")
my_dict = {
    "name": "Ana",
    "age": 18
}

# Add new key "grade"
my_dict["grade"] = "A"

# Update age
my_dict["age"] = 19

# Print all keys
print("Keys:", my_dict.keys())