'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def make_pizza(*toppings):
    print("\nMaking a pizza with following topping(s):")
    for topping in toppings:
        print("- " + topping)
    
    
make_pizza('mushroom')
make_pizza('pepperoni', 'green peppers', 'extra cheese')