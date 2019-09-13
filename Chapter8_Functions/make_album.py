'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def make_album(artist_name, album_title, tracks=''):
    
    if tracks:
        album = {'a_name':artist_name, 'a_title':album_title, 'tracks':tracks}
    else:
        album = {'a_name':artist_name, 'a_title':album_title}
    return album

album_1 = make_album('Shailendra', 'Barsaat')
album_2 = make_album('Amjrooh Sulltanpuri', 'Pyaasa', '21')
album_3 = make_album('Sahir Ludhianavi', 'Milan', '24')

print(album_1)
print(album_2)
print(album_3)