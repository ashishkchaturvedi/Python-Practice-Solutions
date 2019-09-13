'''
Created on Sep 13, 2019

@author: achaturvedi
'''
def make_album(artist_name, album_name, tracks = ''):
    
    album = {'a_name':artist_name, 'album_name':album_name}
    
    if tracks:
        album['tracks'] = tracks
        
    return album

while True:
    print("(enter 'q' at any time to quit)")
    a_name = input("Enter the artist name: ")
    if a_name == 'q':
        break
    
    album_name  = input("Enter the album name: ")
    if album_name == 'q':
        break
    
    tracks = input("Enter tracks if any: ")
    if tracks == 'q':
        break
    
    album =make_album(a_name, album_name, tracks)
    print(album)