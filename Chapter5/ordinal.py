'''
Created on Sep 6, 2019

@author: achaturvedi
'''
numbers = (range(1,10))

for number in numbers:
    if number is 1:
        print(str(number)+"st")
    elif number is 2:
        print(str(number)+"nd")
    elif number is 3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")