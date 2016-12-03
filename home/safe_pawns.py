def safe_pawns(pawns):
    cell = lambda x, y: chr(x) + str(int(y)-1)
    return sum(1 for x, y in pawns if {cell(ord(x)-1, y), cell(ord(x)+1, y)} & pawns)

assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

print('Good')
