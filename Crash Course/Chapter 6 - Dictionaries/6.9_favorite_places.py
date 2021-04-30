"""Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to
three favorite places for each person. Loop through the dictionary and print each persons name and their favorite
places """

favorite_places = {
    'pa': ['italy', 'france', 'rome'],
    'steven': ['philippines', 'jamaica', 'hawaii']
}
for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")