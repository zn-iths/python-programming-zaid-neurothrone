factorial = int(input("Enter a number for n!: "))

total = 1
for num in range(factorial, 1, -1):
    total *= num

print(f"Factorial for {factorial}! = {total}")
print(f"{factorial}! = ", end="")
for num in range(factorial, 0, -1):
    print(f"{num}*" if num > 1 else f"{num}", end="")
print(f" = {total}")
