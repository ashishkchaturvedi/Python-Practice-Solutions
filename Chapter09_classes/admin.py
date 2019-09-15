'''
Created on Sep 14, 2019

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
        print("We are pleased to welcome you: "+ self.first_name + ' ' 
              + self.last_name)
        
class Admin(Users):
    
    def __init__(self, privileges):
        self.privileges = privileges
        self.count = 1
        
    def show_privileges(self):
        print("Admin has following privileges:-")
        for privilege in self.privileges:
            print(str(self.count) + " : " + privilege )
            self.count += 1
            
privileges = ['can add post', 'can delete post', 'can ban user']            

user = Admin(privileges)

user.show_privileges()