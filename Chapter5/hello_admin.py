'''
Created on Sep 6, 2019

@author: achaturvedi
'''
#users = ['admin', 'bunty', 'ramesh', 'suresh', 'dinesh', 'deepu']

users = []

if users:
    for user in users:
        if user is 'admin':
            print("Hello admin, would you like to see a report?")
        else:
            print("Hello "+user+", thank you for logging in again")
else:
    print("Need to find some users")