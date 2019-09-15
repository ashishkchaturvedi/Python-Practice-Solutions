'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('guest.txt', 'w') as file_object:
    name = input("Enter your name: ")
    file_object.write(name)