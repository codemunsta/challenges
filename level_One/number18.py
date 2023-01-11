question = '''
 Write a Python program to calculate the sum of three given numbers, if the values are equal then return
three times of their sum.
'''

# solution

num1 = float(input('number one: '))
num2 = float(input('number two: '))
num3 = float(input('number three: '))


def get_sum(n1, n2, n3):
    if n1 == n2 == n3:
        sum_n = n1 * 3 * 3
    else:
        sum_n = n1 + n2 + n3
    return sum_n


print(get_sum(num1, num2, num3))
