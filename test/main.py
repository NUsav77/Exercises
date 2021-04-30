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

for pet, info in pets.items():
    print(f"{pet.title()} has the following specifications:")
    print(f"\tGender: {info['gender']}")