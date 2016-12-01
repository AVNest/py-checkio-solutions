def _min_max(*it, key=lambda x: x, cmp_func=lambda x, y: x < y):
    if len(it) == 1:
        it = it[0]

    res_val = None
    for val in it:
        if res_val is None or cmp_func(key(val), key(res_val)):
            res_val = val
    return res_val


def min(*it, key=lambda x: x):
    return _min_max(*it, key=key)

def max(*it, key=lambda x: x):
    return _min_max(*it, key=key, cmp_func=lambda x, y: x > y)

assert max(3, 2) == 3
assert min(3, 2) == 2
assert max([1, 2, 0, 3, 4]) == 4
assert min("hello") == "e"
assert max(2.2, 5.6, 5.9, key=int) == 5.6
assert min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
assert min(abs(i) for i in range(-10, 10)) == 0
assert max(filter(str.isalpha, "@v$e56r5CY{]")) == 'v'

print('Good')
