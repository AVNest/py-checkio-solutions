import string
import re

def checkio(text):
    vovels = 'aeiouy'
    key = lambda x: 0 if x in vovels else 1
    return sum(
        all(key(x) != key(y) for x, y in zip(word[::2], word[1::2]))
        for word in re.findall(r'\w+', text) if len(word) > 1
    )
        
assert checkio("My name is ...") == 3
assert checkio("Hello world") == 0
assert checkio("A quantity of striped words.") == 1
assert checkio("Dog,cat,mouse,bird.Human.") == 3
