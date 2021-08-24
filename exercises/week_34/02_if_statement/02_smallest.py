try:
    num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter another number: "))
    smallest = num_1 if num_1 < num_2 else num_2
    print(f"The smallest number is '{smallest}'")
except ValueError:
    print("[Error]: That is not a number.")
