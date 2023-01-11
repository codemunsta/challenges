from math import pi

question = '''
 Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

# solution

# collect radius
radius = float(input('Circle radius: '))


# area function
def circle_area(rad):
    area = pi * (rad ** 2)
    return area


# find area
print(circle_area(radius))
