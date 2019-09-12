'''
Created on Sep 11, 2019

@author: achaturvedi
'''
number = int(input("Enter the number: "))

if number % 10 == 0:
    print("\n" + str(number) +", is multiple of 10.")
else:
    print("\nIt is not a multiple of 10.")