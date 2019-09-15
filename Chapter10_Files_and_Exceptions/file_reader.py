'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())