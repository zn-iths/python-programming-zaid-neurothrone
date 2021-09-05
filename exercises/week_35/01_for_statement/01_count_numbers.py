def count_numbers(steps: int) -> None:
    nums: list[int] = list(range(-10, 10 + 1, steps))
    print(*nums, sep=", ")


count_numbers(steps=1)
count_numbers(steps=2)
