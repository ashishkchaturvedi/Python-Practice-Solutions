'''
Created on Sep 9, 2019

@author: achaturvedi
'''
favorite_language = {
    'Modi':'Java',
    'Amit':'Python',
    'Yogi':'Scala',
    'Arvind':'C',
    }

friend = ['Amit', 'Modi']

for name in favorite_language.keys():
    print("\n"+name.title())
    if name in friend:
        print("Hi "+name.title() +
              ", I see your favotite language is: "+
              favorite_language[name].title()+".")