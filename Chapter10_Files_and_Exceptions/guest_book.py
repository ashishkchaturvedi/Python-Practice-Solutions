'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('guest_book.txt', 'a') as file_object:
    while True:
        message = "Enter your name: "
        message += "(enter 'quit' anytime to quit)"
        name = input(message)
        if name == 'quit':
            break
        file_object.write(name + "\n")
            