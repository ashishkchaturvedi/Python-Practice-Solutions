'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import json

filename = 'username.json'

with open(filename, 'w') as file_obj:
    username = input("Enter your name: ")
    json.dump(username, file_obj)
    
    print("We will remember you name: " + username + "!")