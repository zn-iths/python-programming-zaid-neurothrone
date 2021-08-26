from shared.simulation import roll_dice

simulations: list[int] = []
for _ in range(20):
    simulations.append(roll_dice(1, 6))

FILE_PATH = "../data/dice_rolls.txt"
with open(FILE_PATH, mode="w") as file_out:
    file_out.write("---- Results of 20 dice rolls ----\n")
    file_out.write(str(simulations) + "\n\n")

simulations.sort()
with open(FILE_PATH, mode="a") as file_out:
    file_out.write("---- Results after sorting ----\n")
    file_out.write(str(simulations) + "\n\n")

with open(FILE_PATH, mode="a") as file_out:
    file_out.write("---- Number of fours in the dice rolls ----\n")
    file_out.write(str(simulations.count(4)) + "\n")
