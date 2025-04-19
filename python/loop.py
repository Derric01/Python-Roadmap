# For loop: do something multiple times
for i in range(3):
    print("This is loop number:", i)

# While loop: repeat as long as a condition is true
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# Skipping and breaking out
for i in range(5):
    if i == 2:
        continue  # skip 2
    if i == 4:
        break    # stop the loop
    print("Current i:", i)
