'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def greet_users(names):
    
    for name in names:
        print("\nHello "+name)
        
usernames = ['Modi', 'Amit', 'Arvind']

greet_users(usernames)