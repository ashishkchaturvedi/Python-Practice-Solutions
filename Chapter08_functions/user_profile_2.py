'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def build_profile(first, last, **user_info):
    
    profile = {}
    
    profile['firsst_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

profile = build_profile('Narendra', 'Modi', location = 'Delhi', field = 'Social awarness')

print(profile)