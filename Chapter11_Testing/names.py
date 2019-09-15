'''
Created on Sep 15, 2019

@author: achaturvedi
'''
from Chapter11_Testing import number_function

print("Enter q to exit anytime")

while True:
    first = input("Enter the first name: ")
    if first == 'q':
        break
    
    last = input("Enter last name: ")
    if last == 'q':
        break
    
    formatted_name = number_function.get_formatted_name(first, last)
    
    print("The neatly formatted name is: " + formatted_name)