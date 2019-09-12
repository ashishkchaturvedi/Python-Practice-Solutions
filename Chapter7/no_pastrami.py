'''
Created on Sep 12, 2019

@author: achaturvedi
'''
sandwich_orders = ['pastrami', 'veg', 'pastrami', 'tuna', 'salmon', 'pastrami']

finished_sandwiches = []

print("\nDeli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    

for order in sandwich_orders:
    print("\nI made your "+ order + " sandwich")
    
    finished_sandwiches.append(order)
    
for sandwich in finished_sandwiches:
    print("\n" + sandwich +" sandwich is made")