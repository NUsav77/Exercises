"""Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people,
and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the
list, print everything you know about each person. """

pa_xiong = {
    'first_name': 'pa',
    'last_name': 'xiong',
    'dob': '03/30/1986',
    'city': 'st. paul',
    'ethnicity': 'hmong',
}

evy_nodalo = {
    'first_name': 'evolet',
    'last_name': 'nodalo',
    'dob': '07/07/2020',
    'city': 'san diego',
    'ethnicity': 'filipino/hmong',
}

snodalo = {
    'first_name': 'steven',
    'last_name': 'nodalo',
    'dob': '05/09/1987',
    'city': 'san diego',
    'ethnicity': 'filipino',
}

people = [pa_xiong, evy_nodalo, snodalo]

[print(f"\nFirst name:{person['first_name'].title()}"
       f"\nLast name: {person['last_name'].title()}"
       f"\n\tDate of Birth: {person['dob']}"
       f"\n\tBirth Location: {person['city'].title()}"
       f"\n\tEthnicity: {person['ethnicity'].title()}")for person in people]