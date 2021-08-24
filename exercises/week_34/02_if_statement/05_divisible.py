try:
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")
    print("Is divisible by 5" if num % 5 == 0 else "NOT divisible by 5")
    if num % 5 == 0 and num % 2 == 1:
        print(f"The number {num} is divisible by 5 and is odd.")
    else:
        print(f"The number {num} is NOT divisible by 5 and is NOT odd.")

except ValueError:
    print("[Error]: That is not a number.")
