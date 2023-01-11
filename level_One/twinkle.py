question = '''
Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in
 the sky. Twinkle, twinkle, little star, How I wonder what you are" 
Output :

Twinkle, twinkle, little star,
    How I wonder what you are! 
        Up above the world so high,   		
        Like a diamond in the sky. 
Twinkle, twinkle, little star, 
    How I wonder what you are
'''

# Solution
sample_string = 'Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a ' \
                'diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are'

# break string into substrings
sub1 = 'Twinkle, twinkle, little star,'
sub2 = 'How I wonder what you are'
sub3 = 'Up above the world so high,'
sub4 = 'Like a diamond in the sky. '

# print string using new line and tab formating
print(f'{sub1} \n\t{sub2}! \n\t\t{sub3} \n\t\t{sub4} \n{sub1} \n\t{sub2}')
