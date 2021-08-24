MAX_WEIGHT = 8
MAX_DIMENSIONS = 55 * 40 * 23

try:
    weight = int(input("Enter the weight of your luggage (kg): "))
    length = int(input("Enter the length of your luggage (cm): "))
    width = int(input("Enter the width of your luggage (cm): "))
    height = int(input("Enter the height of your luggage (cm): "))

    if weight <= MAX_WEIGHT and (weight + length + width) <= MAX_DIMENSIONS:
        print("The luggage is allowed.")
    else:
        print("The luggage is NOT allowed.")
except ValueError:
    print("[Error]: That is not a number.")
