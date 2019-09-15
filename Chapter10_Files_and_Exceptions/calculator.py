'''
Created on Sep 15, 2019

@author: achaturvedi
'''
print("Enter two numbers you want to divide: ")
print("(enter 'q' to quit anytime)")

try:
    
    while True:
        num1 = input("Enter first number: ")
        if num1 == 'q':
            break
    
        num2 = input("Enter second number: ")
        if num2 == 'q':
            break
    
        answer = int(num1) / int(num2)
        print(answer)
except ZeroDivisionError:
    print("You can't divide a number by zero")