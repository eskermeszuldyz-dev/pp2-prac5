import math

# 1️ Convert degree to radian
def degree_to_radian(degree):
    return degree * (math.pi / 180)


# 2️ Area of a trapezoid
def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2


# 3️ Area of a regular polygon
def regular_polygon_area(n, side_length):
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))


# 4️ Area of a parallelogram
def parallelogram_area(base, height):
    return base * height



# Test block
if __name__ == "__main__":

    # Task 1
    degree = float(input("Input degree: "))
    radian = degree_to_radian(degree)
    print("Output radian:", round(radian, 6))

    print("\n--------------------")

    # Task 2
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    print("Expected Output:", trapezoid_area(height, base1, base2))

    print("\n--------------------")

    # Task 3
    n = int(input("Input number of sides: "))
    side = float(input("Input the length of a side: "))
    area_polygon = regular_polygon_area(n, side)
    print("The area of the polygon is:", round(area_polygon, 0))

    print("\n--------------------")

    # Task 4
    base = float(input("Length of base: "))
    height_para = float(input("Height of parallelogram: "))
    print("Expected Output:", float(parallelogram_area(base, height_para)))