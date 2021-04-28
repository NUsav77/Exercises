'''
Using one of the programs you wrote in this chapter, add several lines
to the end of the program that do the following:
'''

guest_list = ['pa xiong', 'evolet nodalo', 'wonder woman', 'remy nodalo', 'ashley nodalo', 'tiffany nodalol', 'michael salas ramos']

# Print the message 'The first three items in the list are: '. Then use
# a slice to print the first three items from the program's list.

print('The first three items in the list are: ')
[print(f"{name}".title()) for name in guest_list[:3]]

# Print the message 'Three items from the middle of the list are: '. Use a slice to
# print three items from the middle of the list.

print("Three items from the middle of the list are:")
[print(f"{name}".title()) for name in guest_list[2:5]]