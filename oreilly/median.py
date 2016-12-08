def median(array):
    n = len(array)
    array = sorted(array)
    mid = n // 2
    if not n % 2:
        return sum(array[mid-1:mid+1]) / 2
    else:
        return array[mid]

def checkio(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

assert median([]) == 0 
assert median([1, 2, 3, 4, 5]) == 3
assert median([3, 1, 2, 5, 3]) == 3
assert median([1, 300, 2, 200, 1]) == 2
assert median([3, 6, 20, 99, 10, 15]) == 12.5

print('Good')
