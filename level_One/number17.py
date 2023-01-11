question = '''
Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''

# solution

number = float(input('number to check: '))


def check_num(num):
    check1 = abs(1000-num) <= 100
    if check1:
        return 'number within 100 of 1000'
    else:
        check1 = abs(2000-num) <= 100
        if check1:
            return 'number with 100 of 2000'
        else:
            return 'number out of defined range'


print(check_num(number))
