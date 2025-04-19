# Lists (you can change them later)
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")       # add new item
fruits.remove("banana")      # remove an item

# Tuples (you can't change them)
colors = ("red", "green", "blue")

# Looping through a list
for fruit in fruits:
    print("I like", fruit)

print("Colors available:", colors)
print("I like", colors[0])  # Accessing tuple elements
print("I like", colors[1])  # Accessing tuple elements
print("I like", colors[2])  # Accessing tuple elements
print("I like", colors[0], "and", colors[1])  # Accessing tuple elements
print("I like", colors[0], "and", colors[2])  # Accessing tuple elements
print("I like", colors[1], "and", colors[2])  # Accessing tuple elements
print("I like", colors[0], "and", colors[1], "and", colors[2])  # Accessing tuple elements