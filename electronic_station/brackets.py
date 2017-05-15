""" The solution of https://py.checkio.org/mission/brackets/ task """


def remove_brackets(expr, supported_brackets):
    for brackets in supported_brackets:
        expr = expr.replace(brackets, '')
    return expr


def checkio(expression):
    supported_brackets = ('()', '[]', '{}')
    all_brackets = ''.join(supported_brackets)
    only_brackets = filter(lambda c: c in all_brackets, expression)
    expression = ''.join(only_brackets)

    while True:
        replacement = remove_brackets(expression, supported_brackets)
        if replacement == expression:
            break
        expression = replacement

    return not expression


assert checkio("((5+3)*2+1)") is True
assert checkio("{[(3+1)+2]+}") is True
assert checkio("(3+{1-1)}") is False
assert checkio("[1+1]+(2*2)-{3/3}") is True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") is False
assert checkio("2+3") is True

print('It works')
