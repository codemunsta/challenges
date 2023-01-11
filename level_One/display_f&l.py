question = '''
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''

# solution

color_list = ['Red', 'Green', 'White', 'Black']

# find the length of the list
length_of_list = len(color_list)

# print first and last index elements of list
first_color = color_list[0]
last_color = color_list[length_of_list-1]
print(first_color, last_color)
