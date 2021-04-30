"""Now that you know how to loop through a dictionary, clean up the code frrom exercise 6-3 by replacing your series
of print() calls with a loop that runs through the dictionary's keys and values. When you're sure that your loop
works, add five more Python terms to your glossary. When you run your program again, these new words and meanings
should automatically be included in the output. """

glossary = {
    'get()': 'Checks the dictionary keys. If the key is not present, it gives the user an option to output a '
              'message. Takes in two parameters.',
    'sort()': 'Permanently sorts the list.',
    'sorted()': 'Temporarily sorts the list.',
    'in (keyword)': 'Checks list to see if an item exists.',
    'tuple': 'An immutable list.',
    'set': 'A collection in which each item must be unique.',
    'index()': 'Returns the index of the first element with the specified value.',
    'fromkeys()': 'Returns a dictionary with the specified keys and values.',
}

print('Glossary:')
[print(f"{key}: \n\t{value}") for key, value in sorted(glossary.items())]
