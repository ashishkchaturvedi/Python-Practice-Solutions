'''
Created on Sep 15, 2019

@author: achaturvedi
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")