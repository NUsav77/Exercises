'''Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in oyur dictionary.
Think of a favorite number for each person, and store each as value in your dictionary. Print each person's name and
their favorite number. For even more fun, poll a few friends and get some actual data for your program. '''

favorite_numbers = {
    'steven': 77,
    'pa': 1986,
    'evolet': 330,
    'lorelei': 58,
    'dan': 55,
}

[print(f"{name.title()}'s favorite number is {number}") for name, number in favorite_numbers.items()]