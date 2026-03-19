# Read entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Full content:\n", content)

# Read line by line
with open("sample.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())

# Read lines into list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Lines list:", lines)

# Append new data
with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")

print("Data appended successfully.")

# Verify content
with open("sample.txt", "r") as file:
    print(file.read())    