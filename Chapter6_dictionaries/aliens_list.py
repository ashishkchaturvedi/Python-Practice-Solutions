'''
Created on Sep 9, 2019

@author: achaturvedi
'''
from builtins import str

aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green' , 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)
    
for alien in aliens:
    print(alien)
    
for alien in aliens[5:9]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'

for alien in aliens:
    print(alien)   
print("Total number of aliens: "+ str(len(aliens)))