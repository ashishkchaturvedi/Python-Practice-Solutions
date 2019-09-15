'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('learning_python.txt') as file_objects:
    lines = file_objects.readlines()
    
for line in lines:
    message = line.replace("Python", "C")
    print(message)