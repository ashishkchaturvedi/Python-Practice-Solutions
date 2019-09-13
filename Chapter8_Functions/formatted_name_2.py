'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name+ ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' +last_name 
    return full_name.title()

name1 = get_formatted_name('Ashish', 'Chaturvedi')
name2 = get_formatted_name('Madhaw', 'Chaubey', 'Ji')

print("\n" + name1)
print("\n" + name2)