'''
Created on Sep 9, 2019

@author: achaturvedi
'''
pizza = {
    'crust' : 'thick',
    'Toppings' : ['mushroom' , 'Banana pepper', 'cheese']
    }

print("You orderd a "+pizza['crust']+"-crust pizza" +
      " with the following toppings:")
for topping in pizza['Toppings']:
    print(topping)