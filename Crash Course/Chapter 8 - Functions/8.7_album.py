"""Write a function called make_album() that builds a dictionary describing a music album. The function should take
in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
Use the function to make three Dictionaries representing different albums. Print each return value to show that the
dictionaries are storing the album information correctly. """


def make_album(artist, album):
    album_dict = {
        'artist': artist.title(),
        'album': album.title(),
    }
    return album_dict


tupac = make_album('2pac', 'all eyez on me')
print(f"\nArtist: {tupac['artist']}\n\tGreatest Hit: {tupac['album']}")

snoop = make_album('snoop dogg', 'dogg pound')
print(f"\nArtist: {snoop['artist']}\n\tGreatest Hit: {snoop['album']}")