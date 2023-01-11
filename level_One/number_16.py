question = '''
Write a Python program to get the difference between a given number and 17, if the number is greater 
than 17 return double the absolute difference.
'''

# solution
num = float(input('What is the number: '))


def get_diff(number):
    if number > 17:
        return abs((17-number)*2)
    else:
        return 17-number


print(get_diff(num))
