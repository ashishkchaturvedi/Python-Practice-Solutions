'''
Created on Sep 14, 2019

@author: achaturvedi
'''

from random import randint

class Die():
    
    def __init__(self, value = 6):
        self.dice_value = value
        
    def roll_die(self):
        self.dice_value = randint(1, 6)
        print("The value on 6 side dice is: " + str(self.dice_value))
        
    def roll_ten_sided_die(self):
        self.dice_value = randint(1,10)
        print("The value on 10 side dice is: " + str(self.dice_value))
        
    def roll_twenty_sided_die(self):
        self.dice_value = randint(1,20)
        print("The value on 20 side dice is: " + str(self.dice_value))
        
my_dice = Die()
for x in range(1,11):
    my_dice.roll_die()
    my_dice.roll_ten_sided_die()
    my_dice.roll_twenty_sided_die()
