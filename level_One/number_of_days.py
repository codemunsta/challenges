from datetime import date

question = '''
 Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

# solution
day1 = input('start day: ').replace(" ", '')
day2 = input('end day: ').replace(" ", '')

if '(' in day1:
    day1 = day1.replace('(', '')

if '(' in day2:
    day2 = day2.replace('(', '')

if ')' in day1:
    day1 = day1.replace(')', '')

if ')' in day2:
    day2 = day2.replace('(', '')


start_day = day1.split(",")
end_day = day2.split(",")


def calc_days(start, end):
    try:
        start_year = int(start[0])
        end_year = int(end[0])
    except ValueError:
        raise Exception('input numeric years')
    try:
        start_month = int(start[1])
        end_month = int(end[1])
    except ValueError:
        raise Exception('input numeric months')
    try:
        start_dae = int(start[2])
        end_dae = int(end[2])
    except ValueError:
        raise Exception('input numeric days')

    start = date(start_year, start_month, start_dae)
    end = date(end_year, end_month, end_dae)
    return (end - start).days


print(calc_days(start_day, end_day))
