'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('pi_digits.txt') as file_objects:
    lines = file_objects.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip() + ' '
print(pi_string)
print(len(pi_string))