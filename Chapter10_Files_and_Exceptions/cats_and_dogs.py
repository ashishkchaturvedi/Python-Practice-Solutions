'''
Created on Sep 15, 2019

@author: achaturvedi
'''
def read_file(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("Sorry, we coudln't find the file: "+filename)
    
    else:
        print(content)
        
filenames = ['cats.txt', 'dogs.txt', 'horses.txt']

for file in filenames:
    read_file(file)