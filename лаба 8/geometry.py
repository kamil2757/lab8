import math

def circle_area(radius: float, pi: float = math.pi) -> float:
    return pi * (radius ** 2)

def rectangle_area(length: float, width: float) -> float:
    return length * width

def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height
