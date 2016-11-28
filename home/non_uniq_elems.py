def checkio(array):
    from collections import Counter
    duplicates = {e for e, cnt in Counter(array).items() if cnt > 1}
    return [e for e in array if e in duplicates]

def checkio1(array):
    return [e for e in array if array.count(e) > 1]

print(checkio([1, 2, 3, 1, 3]))
print(checkio1([1, 2, 3, 1, 3]))
