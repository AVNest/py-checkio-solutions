import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    key = lambda x: 0 if x in VOWELS else 1 if x in CONSONANTS else -1
    words = re.findall(r'\w+', text.upper())
    return sum(
        all(key(x) + key(y) == 1 for x, y in zip(word[:len(word)-1:], word[1::]))
        for word in words if len(word) > 1
    )
        
assert checkio("My name is ...") == 3
assert checkio("Hello world") == 0
assert checkio("A quantity of striped words.") == 1
assert checkio("Dog,cat,mouse,bird.Human.") == 3
assert checkio('1st 2a ab3er root rate') == 1

print('Good')
