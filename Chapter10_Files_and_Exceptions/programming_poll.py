'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('programming_poll.txt', 'a') as file_object:
    while True:
        message = 'Please tell why you like programming '
        message += "(enter 'quit' to quit anytime)"
        response = input(message)
        if response == 'quit':
            break
        file_object.write(response + "\n")