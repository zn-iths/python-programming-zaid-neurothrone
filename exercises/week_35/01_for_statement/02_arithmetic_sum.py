def arithmetic_sum(start: int, end: int, steps: int) -> int:
    sum_ = 0
    for num in range(start, end + 1, steps):
        sum_ += num
    return sum_


print(sum(range(1, 100 + 1, 1)))  # 5050
print(sum(range(1, 99 + 1, 2)))   # 2500

print(f"Sum: {arithmetic_sum(start=1, end=100, steps=1)}")
print(f"Sum: {arithmetic_sum(start=1, end=99, steps=2)}")
