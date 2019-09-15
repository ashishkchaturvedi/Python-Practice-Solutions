'''
Created on Sep 9, 2019

@author: achaturvedi
'''
favorite_languages = {
    'Kesari' : ['Scala'],
    'Amit' : ['python', 'ruby'],
    'Modi' : ['c', 'c++'],
    'Arvind' : ['java'],
    'mamta' : ['java', 'scala'],
    }

for name, languages in favorite_languages.items():
    print("\n"+name.title() + "'s favorite languages are:")
    for language in languages:
        print(language)