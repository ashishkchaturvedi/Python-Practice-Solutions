'''
Created on Sep 11, 2019

@author: achaturvedi
'''
prompt = "\nTell me something, ann I will print that for you: "

prompt += "\n Enter 'quit'  to end the program. "

message = ''

active = True

while active == True:
    message = input(prompt)
    
    if message != 'quit':
        print(message)
    
    if message == 'quit':
        active = False