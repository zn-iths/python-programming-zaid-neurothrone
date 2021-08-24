try:
    num = float(input("Enter a number: "))
    if num < 0:
        print(f"The number '{num}' is negative.")
    elif num > 0:
        print(f"The number '{num}' is positive.")
    else:
        print(f"The number '{num}' is zero.")
except ValueError:
    print("[Error]: That is not a number.")
