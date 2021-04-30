"""Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might
be 'nile': 'egypt'. """

rivers = {
    'cagayan river': 'philippines',
    'mississippi river': 'united states of america',
    'yangtze': 'asia',
}

"""Use a loop to print a sentence about each river, such as 'The Nile runs through Egypt'."""

[print(f"The {river.title()} is a famous river that runs through {location.title()}.") for river, location in
 rivers.items()]


"""Use a loop to print the name of each river included in the dictionary."""

print("\nName of famous rivers:\n")
[print(f"{name.title()}") for name in rivers.keys()]

