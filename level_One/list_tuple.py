question = '''
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple 
with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

# solution

# input numbers
numbers = input('Write a list of numbers seperated by commas:')

# split numbers into list and tuple
numbers = numbers.split(',')
tu_numbers = tuple(numbers)

print(numbers, tu_numbers)
