roman_rules = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
               (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
               (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def checkio(num):
    roman_num = ''
    for d, r in roman_rules:
        while num >= d:
            roman_num += r
            num -= d

    return roman_num

def checkio1(num):
    roman_num = ''
    for d, r in roman_rules:
        roman_num += r * (num // d)
        num %= d

    return roman_num



assert checkio1(6) == 'VI'
assert checkio1(76) == 'LXXVI'
assert checkio1(44) == 'XLIV'
assert checkio1(13) == 'XIII'
assert checkio1(3999) == 'MMMCMXCIX'

print('Good')
