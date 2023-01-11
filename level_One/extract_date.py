question = '''
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

# solution
exam_st_date = (11, 12, 2014)

# store date in dictionary
date = {
    'day': exam_st_date[0],
    'month': exam_st_date[1],
    'year': exam_st_date[2]
}

# print using key value pairs in dictionary
print(f'The examination will start from : {date["day"]} / {date["month"]} / {date["year"]}')
