'''
Created on Sep 15, 2019

@author: achaturvedi
'''
def find_common(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("Sorry, but we couldn't locate the file.")
        
    else:
        print(content.lower().count('i'))
        

filename = 'programming.txt'
find_common(filename)
        
