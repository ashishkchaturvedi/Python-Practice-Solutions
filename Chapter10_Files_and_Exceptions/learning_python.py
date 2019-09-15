'''
Created on Sep 15, 2019

@author: achaturvedi
'''
with open('learning_python.txt') as file_objects:
#     contents = file_objects.read()
    lines = file_objects.readlines()
#     for x in range(0,3):
#         print(contents)
#         print()
        
for line in lines:
    print(line)