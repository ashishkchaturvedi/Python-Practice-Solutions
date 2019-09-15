'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def formatted_name(first_name, last_name):
    
    full_name = first_name + ' ' + last_name
    return full_name.title()

programmer = formatted_name('ashish', 'chaturvedi')

print("\nThe name of programmer is: "+programmer)