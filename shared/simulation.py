from random import randint


def roll_dice(min_dice: int, max_dice: int) -> int:
    return randint(min_dice, max_dice)


def simulate_dices(max_simulations: int,
                   min_dice: int,
                   max_dice: int) -> dict[int, int]:
    """Returns a dict with the key: value (dice, frequency)."""
    data: dict[int, int] = dict()
    for key in range(min_dice, max_dice + 1):
        data[key] = 0

    for _ in range(max_simulations):
        rolled_dice = roll_dice(min_dice, max_dice)
        data[rolled_dice] += 1

    return data
