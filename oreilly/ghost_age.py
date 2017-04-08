import math
from itertools import accumulate

def is_fib(x):
    return not (math.sqrt(5 * x**2 + 4) % 1 and math.sqrt(5 * x**2 - 4) % 1)

def checkio(opacity):
    current_opacity = 10**4
    for age in range(5000):
        current_opacity += -age if is_fib(age) else 1
        if current_opacity == opacity:
            return age

def checkio(opacity):
    rates = accumulate(-a if is_fib(a) else 1 for a in range(5000))
    return next(age for age, dec in enumerate(rates) if 10000 + dec == opacity)


print(checkio(10**4))
assert checkio(10000) == 0
assert checkio(9999) == 1
assert checkio(9997) == 2
assert checkio(9994) == 3
assert checkio(9995) == 4
assert checkio(9990) == 5
print('Ghost age calculator works!')
