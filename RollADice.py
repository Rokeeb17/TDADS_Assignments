"""
Project Brief
The Goal of this project, like the title suggests, involves writing a program that simulates rolling a
dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever
other integer you prefer — the number of sides on the die is up to you.) The program will print
what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need
to set the min and max number that your dice can produce. For the average die, that means a
minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number
within that range and prints it.
Concepts to keep in mind:
● Random
● Integer
● Print
● While Loops
"""

import random
#use random integer, print, while loop
minValue = 1
maxValue = 6
#to initialise the variable for the while loop
rollAgain = 'y' 
while rollAgain == 'y' or rollAgain == 'yes':
    print('Rolling the dice')
    diceValue = random.randint(minValue, maxValue)
    print(f'You rolled a {diceValue}!')
    #doesn't work with lowercase y or yes, only works with exact specifed parameters
    rollAgain = input('Wanna roll again? Please type Yes or No: ').lower()
    print('')

print('Thank you for playing!')



