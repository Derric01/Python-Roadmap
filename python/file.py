# Writing to a file (creates file if not exists)
with open("notes.txt", "w") as file:
    file.write("Python is fun!\nLet's keep learning.")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print("File says:")
    print(content)
