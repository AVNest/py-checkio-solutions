import string

def checkio(text):
    vovels = 'aeiouy'
    consonants = set(string.ascii_lowercase) - set(vovels)


assert checkio("My name is ...") == 3
assert checkio("Hello world") == 0
assert checkio("A quantity of striped words.") == 1
assert checkio("Dog,cat,mouse,bird.Human.") == 3
