'''
Created on Sep 15, 2019

@author: achaturvedi
'''
def word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry, but we are unable to find the file:" + filename)
    
    else:
        words = contents.split()
        num_words = len(words)
    
        print("The file " + filename + " has " + str(num_words) + " words.")
    
filename = ['programming.txt', 'guest.txt', 'guest_book.txt', 'abc.txt']

for file in filename:
    word_count(file)

    