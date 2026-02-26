# 1. Squares up to N
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2


# 2. Even numbers up to n
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# 3. Numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# 4. Squares between a and b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


# 5. Countdown generator
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


if __name__ == "__main__":
    print("Squares up to 5:")
    for num in square_generator(5):
        print(num)

    print("\nEven numbers up to 10:")
    print(",".join(str(x) for x in even_numbers(10)))

    print("\nDivisible by 3 and 4 up to 50:")
    for num in divisible_by_3_and_4(50):
        print(num)

    print("\nSquares from 3 to 7:")
    for num in squares(3, 7):
        print(num)

    print("\nCountdown from 5:")
    for num in countdown(5):
        print(num)