from random import randint

random_number = randint(1000, 9999)
total_guesses = 0

for _ in range(9999):
    random_answer = randint(1000, 9999)
    if random_answer == random_number:
        print(f"It took {total_guesses} iterations to get the correct answer of {random_number}.")
        break
    total_guesses += 1
