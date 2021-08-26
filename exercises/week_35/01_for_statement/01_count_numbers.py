def count_numbers(steps: int) -> None:
    for num in range(-10, 10 + 1, steps):
        print(num, end=" ")


count_numbers(steps=1)
print()
count_numbers(steps=2)
