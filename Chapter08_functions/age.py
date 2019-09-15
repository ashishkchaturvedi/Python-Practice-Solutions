'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def build_person(first_name, last_name, age = ''):
    person = {'first_name' : first_name, 'last_name':last_name}
    
    if age:
        person['age'] = age
    return person

name = build_person('ashish', 'Chaturvedi',27)

print(name)