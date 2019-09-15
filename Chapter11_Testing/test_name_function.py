'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import unittest

from Chapter11_Testing import number_function

class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        
        formatted_name = number_function.get_formatted_name('Ashish', 'Chaturvedi')
        
        self.assertEqual(formatted_name, 'Ashish Chaturvedi')
        
    def test_first_middle_last_name(self):
        
        formatted_name = number_function.get_formatted_name('Ashish', 'Chaturvedi', 'Kumar')
        
        self.assertEqual(formatted_name, 'Ashish Kumar Chaturvedi')
        
unittest.main()