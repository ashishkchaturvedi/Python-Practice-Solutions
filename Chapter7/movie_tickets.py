'''
Created on Sep 11, 2019

@author: achaturvedi
'''
prompt = "\nEnter the age of the member:"
prompt += "\nEnter -1 to exit: "

active = True

age = ''

while active == True:
    age = int(input(prompt))
    
    if age >= 0 and age < 3:
        print("\nThe ticket is free.")
    elif age >= 3 and age <= 12:
        print("\nThe ticket price is $10.")
    elif age > 12:
        print("\nThe ticket price is $15.")
    elif age == -1:
        active = False 