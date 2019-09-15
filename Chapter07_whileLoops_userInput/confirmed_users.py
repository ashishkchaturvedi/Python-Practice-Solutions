'''
Created on Sep 11, 2019

@author: achaturvedi
'''
unconfirmed_users = ['Modi', 'Amit', 'Arvind']

confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("\nVerifying user: "+current_user)
    
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print("\t"+confirmed_user)