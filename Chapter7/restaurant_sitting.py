'''
Created on Sep 11, 2019

@author: achaturvedi
'''
people = input("How many people are there in your group: ")
people = int(people)

if people > 8:
    print("\nYou have to wait for sometime.")
else:
    print("\nYou are welcome!")