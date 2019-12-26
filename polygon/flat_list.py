def flat_list(elements):
    for element in elements:
        if isinstance(element, int):
            yield element
        else:
            yield from flat_list(element)


assert list(flat_list(iter([1, 2, 3]))) == [1, 2, 3]
assert list(flat_list(iter([1, iter([2, 2, 2]), 4]))) == [1, 2, 2, 2, 4]
assert list(flat_list(iter([iter([2]), iter([4, iter([5, 6, iter([6]), 6, 6, 6]), 7])]))) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
assert list(flat_list(iter([-1, iter([1, iter([-2]), 1]), -1]))) == [-1, 1, -2, 1, -1]
