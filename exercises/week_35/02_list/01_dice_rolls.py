from random import randint

MIN_DICE_ROLL = 2
MAX_DICE_ROLL = 12

rolls = []

for _ in range(10):
    dice_roll = randint(MIN_DICE_ROLL, MAX_DICE_ROLL)
    rolls.append(dice_roll)

rolls.sort()
print(rolls)

rolls.sort(reverse=True)
print(rolls)

print(f"Min roll: {min(rolls)}")
print(f"Max roll: {max(rolls)}")
