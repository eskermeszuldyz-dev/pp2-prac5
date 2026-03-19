from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map()
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce()
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", sum_all)

# Built-in aggregates
print("len:", len(numbers))
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))