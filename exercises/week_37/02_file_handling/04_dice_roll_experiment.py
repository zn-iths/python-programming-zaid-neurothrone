import json
import pprint

from shared.simulation import simulate_dices

results: dict[int: dict] = dict()
simulations_list = [10 ** exponent for exponent in range(1, 6)]

for simulations in simulations_list:
    frequencies = simulate_dices(max_simulations=simulations,
                                 min_dice=1,
                                 max_dice=6)
    probabilities: dict[int: str] = dict()
    for dice, frequency in frequencies.items():
        probability = (frequency / simulations) * 100
        probabilities[dice] = f"{probability:.2f} %"

    results[simulations] = {
        "frequencies": frequencies,
        "probabilities": probabilities
    }

pp = pprint.PrettyPrinter(width=60)
pp.pprint(results)

with open("../data/simulation.json", mode="w") as file_out:
    json.dump(results, fp=file_out, indent=4)
