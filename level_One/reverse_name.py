question = '''
 Write a Python program which accepts the user's first and last name and print them in reverse order with a space 
 between them.
'''

# solution

# input names from user
firstname = input('Firstname: ')
lastname = input('lastname: ')

# reverse both names
r_firstname = ''.join(reversed(firstname))
r_lastname = ''.join(reversed(lastname))

# display
print(f'{r_lastname} {r_firstname}')
