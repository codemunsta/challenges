question = '''
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
'''

# solution

# input file name
file_name = input('write the name of the file with extension: ')

# split the name using rsplit (rsplit splits a string starting from the right)
name, extension = file_name.rsplit('.', 1)
print(extension)
