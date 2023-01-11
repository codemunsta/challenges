import datetime

question = '''
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''

# solution
date = datetime.datetime.now()

# format time display
date = date.strftime("%Y-%m-%d %H:%M:%S")
print(date)
