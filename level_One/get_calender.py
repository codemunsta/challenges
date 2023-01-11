import calendar

question = '''
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''

# solution
the_month = (input('The month: '))
the_year = input('The year: ')


# get calender
def call_calender(month, year):
    try:
        month = int(month)
    except ValueError:
        month.capitalize()
        match month:
            case 'Jan':
                month = 1
            case 'Feb':
                month = 2
            case 'Mar':
                month = 3
            case _:
                raise Exception('Enter a valid month')

    cal = calendar.month(theyear=int(year), themonth=month)
    return cal


print(call_calender(the_month, the_year))
