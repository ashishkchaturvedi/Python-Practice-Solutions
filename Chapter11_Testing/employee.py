'''
Created on Sep 15, 2019

@author: achaturvedi
'''
class Employee():
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        
    def give_rasie(self, increment = 5000):
        self.salary += increment 