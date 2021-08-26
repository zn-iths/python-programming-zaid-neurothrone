from shared.simulation import simulate_dices

MAX_SIMULATIONS = 1_000_000
dice_frequencies: dict[int, int] = simulate_dices(MAX_SIMULATIONS, 1, 6)

print(f"Total dices of each type in {MAX_SIMULATIONS} amount of simulations.")
for dice_num, value in dice_frequencies.items():
    print(f"Dice [{dice_num}]: {value:,}")
