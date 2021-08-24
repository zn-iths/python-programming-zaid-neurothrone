from random import randint

MIN = 1
MAX = 100
RANDOM_NUM = randint(MIN, MAX)
num_of_guesses = 0

while True:
    try:
        user_guess = int(input(f"Guess a number in the inclusive range of {MIN} to {MAX}: "))
        if user_guess == RANDOM_NUM:
            print("\nCongratulations! You win the game. Program terminating...")
            break
        else:
            num_of_guesses += 1
            if user_guess > RANDOM_NUM:
                print("[Hint]: The number is smaller than your guess.")
            else:
                print("[Hint]: The number is greater than your guess.")
            print(f"You have made {num_of_guesses} guesses so far.\n")
    except ValueError:
        print("[Error]: That is not a number. Try again.")

# Algorithm to as few guesses as possible
# e.g. answer is 52
# guess 1: 50
# guess 2: 75
# guess 3: 60
# guess 4: 55
# guess 5: 53
# guess 6: 52
