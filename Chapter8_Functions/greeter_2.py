'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("\nFirst name: ")
    if f_name == 'q':
        break
    
    l_name = input("\nLast name: ")
    if l_name == 'q':
        break;
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello "+formatted_name)