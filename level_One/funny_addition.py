question = '''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

# solution
n = input('What is your number: ')


# do function to calculate funny n value
def funny_add(number):
    f_add = int(number) + int(number+number) + int(number+number+number)
    return f_add


print(f'Expected Result: {funny_add(n)}')
