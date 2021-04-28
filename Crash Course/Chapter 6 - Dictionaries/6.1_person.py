"""Use a dictionary to store information about a person you know. Store their first name, last name, age,
and the city in which they live. You should have keys such as first_name, las_name, age, and city. Print each piece
of information stored in your dictionary. """

pa_xiong = {
    'first_name': 'pa',
    'last_name': 'xiong',
    'dob': '3/30/1986',
    'city': 'st. paul',
}

[print(f"{key}: {value}".title().strip('_')) for key, value in pa_xiong.items()]