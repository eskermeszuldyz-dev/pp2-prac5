# *args and **kwargs

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    print(total)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

sum_all(1, 2, 3, 4)
print_info(name="Zhuldyz", age=18)