from math import factorial as fac


def N(p, q):
    result = 0
    for n in range(q):
        result += T(n,p) * (p**n)
    return result


def Nfac(p, q):
    return fac(N(p,q))


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1

    return factors


def count_primes(p, list_):
    return sum(n == p for n in list_)


def NF(p, q):
    prime_facs = prime_factors(Nfac(p, q))
    return count_primes(p, prime_facs)

###############
p, q = 61, 10**7
s = 290797
sum = 0
for n in range(1, q + 1):
    s = s**2 % 51515093
    t = s % p
    sum += t * (p ** n)

factors = []
for n in range(1, sum + 1):
    if n % p == 0:
        factors.append(prime_factors(n))

print(count_primes(p, factors))
