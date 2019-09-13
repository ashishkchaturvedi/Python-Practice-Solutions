'''
Created on Sep 12, 2019

@author: achaturvedi
'''
def describe_city(name, country = 'India'):
    print("\n" + name + ', is in ' + country)
    
describe_city('Delhi')
describe_city('Mumbai')
describe_city('Boston', 'USA')