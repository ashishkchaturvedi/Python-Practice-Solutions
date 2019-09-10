'''
Created on Sep 6, 2019

@author: achaturvedi
'''
current_users = ['Rabish', 'Barkha', 'Modi', 'Amit', 'Arvind']

new_users = ['Amit', 'Vasco', 'Gama', 'Nitish', 'BARKHA']

if new_users and current_users:
    for user in new_users:
        if user.title() in current_users:
            print("Username is not available, Enter a new username\n")
        else:
            print("Username is available\n")
else:
    print("Need to add some users")