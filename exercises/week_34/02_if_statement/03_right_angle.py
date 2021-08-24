MAX_DEGREES = 180
RIGHT_ANGLE = 90

try:
    angle_1 = int(input("Enter an angle: "))
    angle_2 = int(input("Enter a second angle: "))
    angle_3 = int(input("Enter a third angle: "))

    if angle_1 + angle_2 + angle_3 != MAX_DEGREES:
        print(f"That is not a triangle. The angles must sum up to a max of {MAX_DEGREES}")
        exit()

    if angle_1 <= 0 or angle_2 <= 0 or angle_3 <= 0:
        print("Not all angles are valid.")
        exit()

    if angle_1 == RIGHT_ANGLE or angle_2 == RIGHT_ANGLE or angle_3 == RIGHT_ANGLE:
        print("The triangle has a right angle.")
    else:
        print("The triangle does not have a right angle.")
except ValueError:
    print("[Error]: That is not a number.")
