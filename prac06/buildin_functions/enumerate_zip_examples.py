names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate()
for index, name in enumerate(names):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# sorted()
numbers = [5, 2, 9, 1]
print("Sorted:", sorted(numbers))

# Type conversions
num_str = "123"
num_int = int(num_str)
print("Converted to int:", num_int)
print("Type:", type(num_int))