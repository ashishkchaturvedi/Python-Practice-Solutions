'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import json

filename = 'username.json'

with open(filename) as file_obj:
    username = json.load(file_obj)
    
    print("Welcome back " + username + "!")