'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def make_sandwich(*items):
    print("\nMaking your sandwich with following items: ")
    for item in items:
        print(item)

make_sandwich('Cheese')
make_sandwich('Pannner', 'Onion', 'Tomato', 'Tikka')
make_sandwich('Samosa', 'Onion', 'Tomato', 'Panner', 'Chilli', 'veg patty')