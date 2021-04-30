"""Write a function called describe_city() that accepts the name of a city and its country. The function should print
a simple sentence, such as "San Diego is in United State". Give the parameter for the country a default value. Call
your function for three different cities, at least one of which is not in the default country. """


def describe_city(city, country='united states of america'):
    print(f"{city.title()} is located in {country.title()}.")


san_diego = describe_city('san diego')

manila = describe_city('manila', 'philippines')

paris = describe_city('paris', 'france')