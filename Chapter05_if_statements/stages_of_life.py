'''
Created on Sep 6, 2019

@author: achaturvedi
'''
age = 65

if age < 2:
    print("Person is a baby")
elif age >= 2 and age < 4:
    print("Person is a toddler")
elif age >= 4 and age < 13:
    print("Person is a kid")
elif age >= 13 and age < 20:
    print("Person is teenager")
elif age >= 20 and age < 65:
    print("Person is adult")
elif age >= 65:
    print("Person is elder")