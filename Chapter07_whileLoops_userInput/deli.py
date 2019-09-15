'''
Created on Sep 12, 2019

@author: achaturvedi
'''
sandwich_orders = ['veg', 'tuna', 'salmon']

finished_sandwiches = []

for order in sandwich_orders:
    print("\nI made your "+ order + " sandwich")
    
    finished_sandwiches.append(order)
    
for sandwich in finished_sandwiches:
    print("\n" + sandwich +" sandwich is made")