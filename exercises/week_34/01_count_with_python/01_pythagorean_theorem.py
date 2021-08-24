from math import pow
from math import sqrt


def compute_hypotenuse(a: int, b: int) -> float:
    # formula: c^2 = a^2 + b^2
    return sqrt(pow(a, 2) + pow(b, 2))


def compute_other_cathetus(cathetus: float, hypotenuse: float) -> float:
    return sqrt(pow(hypotenuse, 2) - pow(cathetus, 2))


print(f"Hypotenuse: {compute_hypotenuse(a=3, b=4)}")
print(f"Cathetus: {compute_other_cathetus(cathetus=5.0, hypotenuse=7.0):.1f}")
