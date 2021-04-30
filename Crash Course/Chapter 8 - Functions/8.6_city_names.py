"""Write a function called city_country() that takes in the name of a city and its country. The function should
return a string formatted like this 'San Diego, USA'. Call your function with at least three city_country pairs and
print the values that are returned. """

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country('san diego', 'united states of america'))

pa_hometown = city_country('st. paul', country='united states of america')
print(pa_hometown)