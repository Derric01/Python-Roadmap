# Dictionary: like a mini-database of key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person["name"])        # get value by key
person["age"] = 31           # update value

# Set: only unique items
numbers = {1, 2, 2, 3}
numbers.add(4)

print("Person info:", person)
print("Unique numbers:", numbers)
print("Is 2 in numbers?", 2 in numbers)  # check membership
print("Is 5 in numbers?", 5 in numbers)  # check membership