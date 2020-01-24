import re
import string
from collections import Counter


def checkio(text: str) -> str:
    lower_text = text.lower()
    chars = ''.join(re.findall(r'[a-z]+', lower_text))
    char_statistics = Counter(chars)
    best_char, _ = max(char_statistics.items(), key=lambda x: (x[1], -ord(x[0])))
    
    return best_char


def checkio1(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


assert checkio("Hello World!") == "l", "Hello test"
assert checkio("How do you do?") == "o", "O is most wanted"
assert checkio("One") == "e", "All letter only once."
assert checkio("Oops!") == "o", "Don't forget about lower case."
assert checkio("AAaooo!!!!") == "a", "Only letters."
assert checkio("abe") == "a", "The First."
print("Start the long test")
assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
print("The local tests are done.")
