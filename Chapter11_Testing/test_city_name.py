'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import unittest

from Chapter11_Testing import city_country

class CityNameTest(unittest.TestCase):
    
    def test_location_name(self):
        
        location = city_country.get_formatted_name('Delhi', 'India')
        
        self.assertEqual(location, 'Delhi, India')
        
    def test_location_population(self):
        
        location = city_country.get_formatted_name('delhi', 'India', 'population 500000')
        
        self.assertEqual(location, 'Delhi, India - Population 500000')
        
unittest.main()