'''
Created on Sep 15, 2019

@author: achaturvedi
'''
def addition():
    
    try:
        while True:
            print("Enter two numbers to add")
            print("(enter 'q' anytime you want to quit)")
            
            num1 = input("Enter first number: ")
            if num1 == 'q':
                break
        
            num2 = input("Enter second number: ")
            if num2 == 'q':
                break
            
            addition = int(num1) + int(num2)
            print(addition)
    except ValueError:
        print("You can't enter String at place of Integer")

        
addition()