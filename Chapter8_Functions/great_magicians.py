'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def make_great(magicians):
    while magicians:
        magician = magicians.pop()
        change = 'Great ' + magician
        modified_magcians.append(change)
    return modified_magcians   
        

def show_magicians(modified_magcians):
    for magician in modified_magcians:
        print(magician) 
        
magicians = ['sarkar', 'majumdar', 'clinton']

modified_magcians = []
modification = make_great(magicians)
show_magicians(modification)
