def checkio(field):
    print(field)

    
assert checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
assert checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
assert checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"

print('Good')
