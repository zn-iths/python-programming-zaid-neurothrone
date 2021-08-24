def even_convergence(max_exponent: int) -> int:
    sum_ = 1
    base = 2
    exponent = 1
    while exponent <= max_exponent:
        sum_ += 1 / (base ** exponent)
        exponent += 1
    return sum_


def odd_convergence(max_exponent: int) -> int:
    sum_ = 1
    n = 1

    while n <= max_exponent:
        quotient = (-1) ** 2
        dividend = (2 * n) + 1
        sum_ += quotient / dividend
        n += 1
    return sum_


print(even_convergence(max_exponent=10))
print(odd_convergence(max_exponent=10))
