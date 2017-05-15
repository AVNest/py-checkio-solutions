""" The solution of https://py.checkio.org/mission/largest-histogram/ task """


# V1.
def largest_histogram_v1(histogram):
    squares = set()
    max_width = len(histogram)
    for col, height in enumerate(histogram):
        for height in range(height, 0, -1):
            width = next((c for c, h in enumerate(histogram[col:])
                          if height > h), max_width-col)
            squares.add(height * width)
    return max(squares)


# V2.
def squares_gen(area):
    """ Generator of rectangle squares for the area """
    area_width = len(area)
    for height in range(area[0], 0, -1):
        width = next((c for c, h in enumerate(area)
                      if height > h), area_width)
        yield width * height


def largest_histogram_v2(histogram):
    max_width = len(histogram)
    squares = (max(squares_gen(area=histogram[col:]))
               for col in range(max_width))
    return max(squares)


# V3. Not mine.
def largest_histogram(histogram):
    n = len(histogram)
    return max((col_end - col_start) * min(histogram[col_start:col_end])
               for col_start in range(n)
               for col_end in range(col_start+1, n+1))


assert largest_histogram([5]) == 5
assert largest_histogram([5, 3]) == 6
assert largest_histogram([1, 1, 4, 1]) == 4
assert largest_histogram([1, 1, 3, 1]) == 4
assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
print('Works good!')
