'''
Created on Sep 15, 2019

@author: achaturvedi
'''

file_path = 'C:/Users/achaturvedi/Documents/Python-Programs/ehmatthes-pcc_2e-4002a3c/ehmatthes-pcc_2e-4002a3c/chapter_10/pi_million_digits.txt'

with open(file_path) as file_objects:
    contents = file_objects.readlines()

pi_string = ''
for content in contents:
    pi_string += content.rstrip()
    
birthday  = input("Enter your birthday on form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in first million digits of pi")
else:
    print("Your birthday doesn't appear in first million digits of pi")