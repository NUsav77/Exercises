'''
Start with your program from Exercise 4.1.
Make a copy of the list of pizzas, and call it friend_pizzas.
Then do the following:
'''

fav_pizzas = ['supreme', 'stuffed crust', 'pan', 'thin crust', 'hawaiian', 'bbq chicken']
friend_pizzas = fav_pizzas[:]

# Add a new pizza to the original list

fav_pizzas.append('meat lovers')

# Add a different pizza to the list friend_pizzas:

friend_pizzas.append('vegetarian')

# Prove that you have two separate lists. Print the message
# "My favorite pizzas are:" and then use a for loop to print the first list.
# Print the message "My friend's favorite pizzas are:" and then use a for loop to print the
# second list. Make sure each new pizza is stored in the appropriate list.

print("\nMy favorite pizzas are: ")
[print(f"{pizza}".title()) for pizza in fav_pizzas]

print("\nMy friend's favorite pizzas are:")
[print(f"{pizza}".title()) for pizza in friend_pizzas]