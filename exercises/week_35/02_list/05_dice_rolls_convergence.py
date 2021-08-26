from random import randint
from random import seed

import matplotlib.pyplot as plt


def compute_dice_outcome(iterations: int, dice: int) -> int:
    dice_rolls = [randint(1, 6) for _ in range(iterations)]
    return dice_rolls.count(dice)


def compute_dice_probability(iterations: int, outcomes: int) -> float:
    return outcomes / iterations


seed(1)

print("A)")
outcome_a = compute_dice_outcome(iterations=100, dice=6)
print(f"100 dice rolls rolled the dice [6] {outcome_a} times.\n")

print("B)")
# 10, 100, 1000, 10 000, 100 000, 1 000 000
iterations_list = [10 ** exponent for exponent in range(1, 6 + 1)]
outcomes_list = [compute_dice_outcome(iterations=iterations,
                                      dice=6) for iterations in iterations_list]
probabilities = [compute_dice_probability(iterations=iterations,
                                          outcomes=outcomes) for iterations, outcomes in
                 zip(iterations_list, outcomes_list)]


print(f"iterations = {iterations_list}")
print(f"outcomes = {outcomes_list}")
print(f"probabilities = {probabilities}")


plt.plot(probabilities, color="purple")
plt.title("Probability for rolling [6] on different number of iterations")
plt.xlabel("Dice rolls")
plt.ylabel("Probability")
plt.xticks(list(range(0, 6)), iterations_list)
plt.show()
