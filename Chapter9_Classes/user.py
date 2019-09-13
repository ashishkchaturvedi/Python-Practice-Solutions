'''
Created on Sep 13, 2019

@author: achaturvedi
'''
class Users():
    def __init__(self, first_name, last_name, location, field):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.field = field

    def describe_user(self):
        print("\nThe name of person is: "  + self.first_name + ' ' + self.last_name)
        print("He lives in: "+self.location)
        print("And workes in the " + self.field + " field")

    def greet_user(self):
        print("We are pleased to welcome you: "+ self.first_name + ' ' + self.last_name)
        
user1 = Users('Narendra', 'Modi', 'Delhi', 'Social Awarness')
user2 = Users('Amit', 'Shah', 'Ahmedabad', 'Public Administration')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()