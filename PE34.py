"""Solution for Problem 34 on Project Euler."""

from math import factorial as fac


def fact_digit():
    """Sum all numbers who's digit factorial sum is the original number."""
    f = {str(x): fac(x) for x in range(10)}
    result = []

    for n in range(10, 50000):
        n_sum = sum(f[digit] for digit in str(n))
        if n_sum == n:
            result.append(n)
    return sum(result)

print(fact_digit())
