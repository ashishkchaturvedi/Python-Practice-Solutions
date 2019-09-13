'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def print_models(unprinted_models, completed_models):
    
    while unprinted_models:
        current_model = unprinted_models.pop()
        
        print("\nPrinting model: "+current_model)
        completed_models.append(current_model)
        
def show_completed_models(completed_models):
    
    print("\nFollowing models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_models = ['iphone', 'Samsung', 'Oppo']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)