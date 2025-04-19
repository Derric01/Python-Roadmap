# List Comprehension: quick way to make a list
squares = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]
print("Squares:", squares)

# Lambda: mini function in one line
add = lambda a, b: a + b
print("3 + 5 =", add(3, 5))

# Error handling
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Oops! Can't divide by zero.")
finally:
    print("Done trying.")
