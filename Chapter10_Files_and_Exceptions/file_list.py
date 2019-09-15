'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('pi_digits.txt') as file_objects:
    lines = file_objects.readlines()
    
for line in lines:
    print(line.rstrip() )