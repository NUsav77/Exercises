"""Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind
of animal and the owner's name. Store these dictionaries in a dictionary called pets. Next, loop through your
dictionary and as you do, print everything you know about each pet. """

pets = {
    'remy': {
        'gender': 'female',
        'species': 'dog',
        'breed': 'husky',
        'color': 'black/white',
        'age': 4,
    },
    'martin': {
        'gender': 'male',
        'species': 'cat',
        'breed': 'tuxedo',
        'color': 'black/white',
        'age': 1,
    },
}

[print(f"\n{pet.title()}\n\tGender: {pet_info['gender']}"
       f"\n\tSpecies: {pet_info['species']}"
       f"\n\tBreed: {pet_info['breed']}"
       f"\n\tColor: {pet_info['color']}"
       f"\n\tAge: {pet_info['age']}") for pet, pet_info in pets.items()]
