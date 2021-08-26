def is_four_digit(num: int) -> bool:
    num_str = str(num).replace("-", "")
    return True if len(num_str) == 4 else False


# test program
test_numbers = [231, 3124, -4124, -1000, -999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_four_digit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")
