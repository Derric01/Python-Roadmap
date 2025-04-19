# Let's check if someone is old enough to vote
age = 16

if age >= 18:
    print("You're eligible to vote!")
elif age >= 13:
    print("You're a teenager!")
else:
    print("You're a kid!")

# Logical Operators: and, or, not
has_id = True
has_ticket = False

if has_id and has_ticket:
    print("You may enter.")
else:
    print("Sorry, access denied.")
