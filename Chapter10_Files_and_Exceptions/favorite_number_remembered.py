'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import json

filename = 'numbers2.json'
try:
    
    with open(filename) as file_obj:
        number = json.load(file_obj)
    
        print(number)

except:
    number = input("Enter your favorite number")
    
    filename = 'numbers2.json'
    
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)