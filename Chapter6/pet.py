'''
Created on Sep 10, 2019

@author: achaturvedi
'''
Robert = {'Owner' : 'Dhanajaya', 'Kind' : 'Dog'}
Chuimui = {'Owner' : 'Ghanshyam', 'Kind' : 'Cat'}
Bichkutiya = {'Owner' : 'Naresh', 'Kind' : 'Lizard'}

pets = [Robert, Chuimui, Bichkutiya]

for pet in pets:
    print("\nOwner is: "+pet['Owner'])
    print("The pet is: "+pet['Kind'])