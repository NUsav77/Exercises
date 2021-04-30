

"""Start with your program from exercise 8.7. Write a while loop that allows users to enter an album's artist and
title. Once you have that information, call make_album() with the user's input and print the dictionary that's
created. Be sure to include a quit value in the while loop. """


def make_album(artist, album):
    album_dict = {
        'artist': artist.title(),
        'album': album.title(),
    }
    return album_dict


while True:
    print("Enter 'quit' whenever you're done.")
    user_artist = input('Enter your favorite artist: ')
    if user_artist == 'quit':
        break
    user_album = input('Enter your favorite album: ')
    print("\n", make_album(user_artist, user_album), '\n')
