'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import unittest

from Chapter11_Testing.employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.my_emp = Employee('Ashish', 'Chaturvedi', 185000)
        
    def test_raise_default(self):
        self.my_emp.give_rasie()
        
    def test_raise(self):
        self.my_emp.give_rasie(6000)
        
unittest.main()