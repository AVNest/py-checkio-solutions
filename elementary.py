# 1. Fizz Buzz
def checkio(x):
    div_to_3, div_to_5 = not x % 3, not x % 5
    return ('Fizz Buzz' if div_to_3 and div_to_5 else
            'Fizz' if div_to_3 else 'Buzz' if div_to_5 else str(x))


assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(5) == "Buzz"
assert checkio(7) == "7"
print('1. Fizz Buzz works!')


# 2. Index Power
def index_power(data, i):
    return data[i] ** i if 0 <= i < len(data) else -1


assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1
print('2. Index power works!')


# 3. Even the last
def checkio(array):
    return sum(array[::2]) * array[-1] if array else 0


assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0
print('3. Even the last works!')


# 4. Find the message
def find_message(msg):
    return ''.join(c for c in msg if c.isupper())


assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
assert find_message("hello world!") == ""
print('4. Find message works!')


# 5. Three words in row
def checkio(text):
    tokens = text.split()
    n = len(tokens)
    return any(1 for i in range(n) if n >= i+3
               if all(not t.isnumeric() for t in tokens[i:i+3]))


# or
def checkio(text):
    return "www" in "".join('w' if w.isalpha() else 'd' for w in text.split())


assert checkio("Hello World hello") is True
assert checkio("He is 123 man") is False
assert checkio("1 2 3 4") is False
assert checkio("bla bla bla bla") is True
assert checkio("Hi") is False
print('5. Three words in row works!')


# 6. Max - Min
def checkio(*seq):
    return round(max(seq) - min(seq), 3) if seq else 0


assert checkio(1, 2, 3) == 2
assert checkio(5, -5) == 10
assert checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
assert checkio() == 0
print('6. Max - Min works!')


# 7. Right to Left
def left_join(words):
    return ','.join(w.replace('right', 'left') for w in words)


assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"
print('7. Right to left works!')


# 8. Digits multiplication
def checkio(x):
    import operator
    from functools import reduce
    return reduce(operator.mul, map(int, str(x).replace('0', '')))


assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1
print('8. Digits multiplication works!')


# 9. Number base convert
def checkio(x, base):
    try:
        return int(x, base)
    except ValueError:
        return -1


assert checkio("AF", 16) == 175
assert checkio("101", 2) == 5
assert checkio("101", 5) == 26
assert checkio("Z", 36) == 35
assert checkio("AB", 10) == -1
print('9. Number base works!')


# 10. ABS sorting
def checkio(array):
    return sorted(array, key=abs)


assert checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20] # or (-5, 10, 15, -20)
assert checkio((1, 2, 3, 0)) == [0, 1, 2, 3]
assert checkio((-1, -2, -3, 0)) == [0, -1, -2, -3]
print('10. ABS sorting works!')


# 12. Second index
def second_index(text: str, symbol: str) -> [int, None]:
    try:
        first_occurrence_index = text.index(symbol)
        return text.index(symbol, first_occurrence_index + 1)
    except ValueError:
        return None


assert second_index("sims", "s") == 3, "First"
assert second_index("find the river", "e") == 12, "Second"
assert second_index("hi", " ") is None, "Third"
assert second_index("hi mayor", " ") is None, "Fourth"
assert second_index("hi mr Mayor", " ") == 5, "Fifth"


# 13. First word:
def first_word(text: str) -> str:
    words = text.split()
    return words[0]

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("hi") == "hi"


# 14. Bigger price
from operator import itemgetter


def bigger_price(limit: int, data: list) -> list:
    sorted_data = sorted(data, key=itemgetter('price'), reverse=True)
    return sorted_data[:limit]

assert bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
], "First"

assert bigger_price(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}], "Second"

