try:
    age = int(input("Enter your age (in years): "))
    weight = int(input("Enter your weight (in kg): "))

    if age > 12 and weight > 40:
        print("It is recommended that you take 1-2 pills.")
    elif 7 <= age <= 12 and 26 <= weight <= 40:
        print("It is recommended that you take half a pill or just one.")
    elif 3 <= age <= 7 and 15 <= weight <= 25:
        print("It is recommended that you only take half a pill.")
    else:
        print("No recommendations for this, seek medical consultation at once!")
except ValueError:
    print("[Error]: That is not a number. Only enter numbers.")
