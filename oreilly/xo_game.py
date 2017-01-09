def checkio(data):
    n = len(data)
    rows = data
    cols = list(zip(*data))
    diagonal1 = [r[i] for i, r in enumerate(data)]
    diagonal2 = [r[i] for i, r in zip(range(n-1, -1, -1), data)]
    testing_variants = rows + cols + [diagonal1, diagonal2]
    for player in 'XO':
        if any((all(e == player for e in variant) for variant in testing_variants)):
            return player

    return 'D'

    
assert checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
assert checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
assert checkio([
    "OO.",
    "XOX",
    "XXO"]) == "O"
assert checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"

print('Good')
