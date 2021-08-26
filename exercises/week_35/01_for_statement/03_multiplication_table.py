def print_multiplication_table(table: int, start: int, end: int) -> None:
    for num in range(start, end + 1):
        print(f"{table * num:4}", end=" ")


try:
    table_ = int(input("Enter table number: "))
    start_ = int(input("Enter start number to start multiplying with: "))
    end_ = int(input("Enter end number to stop multiplying with: "))
    print_multiplication_table(table=table_, start=start_, end=end_)
except ValueError:
    print("[Error]: Only enter integers.")

print()
print()

print("Full multiplication table:")
for number in range(0, 10 + 1):
    print_multiplication_table(table=number, start=0, end=10)
    print()
