"""Write a program that polls users about their dream vacation. Write a prompt similar to 'if you could visit one
place in the world, where would you go?' Include a block of code that prints the results of the poll. """

place = str
places = []
active = True

while active:
    if place == 'quit':
        [print(place.title()) for place in places]
        active = False

    place = input('If you could visit one place in the world, where would you go?\n'
                  '(type "quit" to end): ')

    if place != 'quit':
        places.append(place)
