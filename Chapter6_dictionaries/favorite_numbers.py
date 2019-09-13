'''
Created on Sep 9, 2019

@author: achaturvedi
'''
favorite_numbers = {
    'Akhil' : 2,
    'Diwakar' : 19,
    'Saket': 34,
    'Vishwas' : 56,
    }

print(favorite_numbers)

for name, number in favorite_numbers.items():
    print("\nName: "+name)
    print("Favorite_Number: "+str(number))