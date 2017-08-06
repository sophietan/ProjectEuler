"""Solution for Problem 1 on Project Euler."""


def sum_divisors(x: int):
    """Sum numbers divisible by 3 or 5 up to max number x."""
    num = []

    for y in range(x):
        if y % 3 == 0 or y % 5 == 0:
            num.append(y)
    return sum(num)

print(sum_divisors(1000))
