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

assert checkio("((5+3)*2+1)") == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("2+3") == True

print('It works')
