question = '''
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

# solution

# funk = str(input('function to get info: '))


def get_help(func) -> str:
    if func.endswith('()'):
        name, _ = func.rsplit('()', 1)
    else:
        name = func
    return help(name)


def get_help2(func) -> str:
    if func.endswith('()'):
        name, _ = func.rsplit('()', 1)
    else:
        name = func
        return name.__doc__


# print(get_help(funk))
# print(get_help2(funk))
print(abs.__doc__)

