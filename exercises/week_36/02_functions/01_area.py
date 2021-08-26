def triangle_area(base: float, height: float) -> float:
    """Returns the area of a triangle."""
    return (base * height) / 2


base_ = 3.5
height_ = 5
area = triangle_area(base_, height_)
print(f"The area of a triangle with the base [{base_}] and height [{height_}] is [{area}].")
