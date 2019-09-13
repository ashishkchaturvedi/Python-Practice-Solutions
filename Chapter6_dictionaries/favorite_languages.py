'''
Created on Sep 9, 2019

@author: achaturvedi
'''
favorite_language ={
    'Modi':'Java',
    'Amit':'Python',
    'Yogi':'Scala',
    'Arvind':'C',
    }

print(favorite_language)
print("Amit's favorite language is: "+favorite_language['Amit'].upper())

for name in favorite_language.keys():
    print(name.title())