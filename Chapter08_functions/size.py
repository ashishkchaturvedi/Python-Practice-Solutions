'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with following topping(s): ")
    for topping in toppings:
        print(topping)
        
make_pizza(12, 'mushroom')
make_pizza(18, 'mushroom', 'pineapple', 'banana pepper')