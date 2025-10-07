import math

def square(side):
    square = side**2
    return square
side = float(input())
result = square(side)
rounded = math.ceil(result)
print(rounded)
