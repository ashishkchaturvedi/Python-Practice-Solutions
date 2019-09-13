'''
Created on Sep 5, 2019

@author: achaturvedi
'''
my_foods = ['Paneer makhani', 'Tandoori roti', 'Kaju paneer', 'Garlic naan']

friend_foods = my_foods[:]

my_foods.append('Daal makhani')

friend_foods.append('Egg curry')

print("My Favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n")

for food in my_foods:
    print(food)
    
for food in friend_foods:
    print(food)