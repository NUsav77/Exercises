"""A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.

- Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your
glossary, and store their meanings as values.

- Print each word and its meaning as neatly formatted output. You might print the word followed by a colo and then
its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline \n
character to insert a blank line between each word-meaning pair in your output """

glossary = {
    '.get()': 'Checks the dictionary keys. If the key is not present, it gives the user an option to output a '
              'message. Takes in two parameters.',
    '.sort()': 'Permanently sorts the list.',
    '.sorted()': 'Temporarily sorts the list.',
    'keyword in': 'Checks list to see if an item exists.',
    'tuple': 'An immutable list.',
}

[print(f"{key}: \n\t{value}\n") for key, value in sorted(glossary.items())]