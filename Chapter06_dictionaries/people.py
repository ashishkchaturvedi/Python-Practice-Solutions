'''
Created on Sep 10, 2019

@author: achaturvedi
'''

people_1 = {'Name' : 'Sudhir', 'Age' : 25}

people_2 = {'Name' : 'Deepak', 'Age' : 37}

people_3 = {'Name' : 'Ghanshyam', 'Age' : 24}

peoples = [people_1, people_2, people_3]

for people in peoples:
    print("\nName is: "+people['Name'])
    print("Age is: "+str(people['Age']))
    