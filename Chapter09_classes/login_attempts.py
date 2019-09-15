'''
Created on Sep 13, 2019

@author: achaturvedi
'''
class Users():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.login_attempts = 0
        
    def describe_user(self):
        print("\nThe name of user is: " + self.first_name + ' ' + self.last_name)
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("The total login attempts till now are: " + str(self.login_attempts))
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Re-setted the login attempts to: " + str(self.login_attempts))
        
    
user1 = Users("Ashish", "Chaturvedi")
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()