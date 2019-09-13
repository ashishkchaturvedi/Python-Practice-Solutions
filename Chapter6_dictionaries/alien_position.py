'''
Created on Sep 9, 2019

@author: achaturvedi
'''
alien_0={'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x_position: "+str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
if alien_0['speed'] == 'medium':
    x_increment = 2
if alien_0['speed'] == 'high':
    x_increment = 3
    
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position is: "+ str(alien_0['x_position']))