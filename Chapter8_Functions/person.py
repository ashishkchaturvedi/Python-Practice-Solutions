'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def build_person(first_name, last_name):
    person = {'first_name' : first_name, 'last_name':last_name}
    return person

name = build_person('ashish', 'Chaturvedi')

print(name)