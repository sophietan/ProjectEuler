def sgn(a):
    return 1 if a > 0 else -1


def f(x):
    a = 903 * (1 + x ** 4999)/(1 + x)
    b = (3 * x * (1 - 5000 * x ** 4999 + 4999 * x ** 5000)) / (1 - x)**2
    return a - b + 600_000_000_000

def bisect(a,b):
    c = (a + b)/2
    f_a = f(a)
    f_b = f(b)
    f_c = f(c)
    
    if sgn(f_a) != sgn(f_c):
        if abs(f_a - f_c) < 1e-13:
            return c
        return bisect(a, c)
    elif sgn(f_b) != sgn(f_c):
        if abs(f_b - f_c) < 1e13:
            return c
        return bisect(b, c)
    else:
        raise Exception('wrong interval')
    
print(bisect(-2, 2))
