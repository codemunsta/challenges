from math import pi, pow
question = '''
Write a Python program to get the volume of a sphere with radius 6.
'''

# solution
rad = float(input('radius of sphere: '))


# volume = 4/3pi(r**3)
def sphere_volume(radius):
    volume = 4 / 3 * pi * (pow(radius, 3))
    return volume


print(sphere_volume(rad))
