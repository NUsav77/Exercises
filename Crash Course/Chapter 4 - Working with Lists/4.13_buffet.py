'''
A buffet style restaurant offers only five basic foods. Think of five simple
foods, and store them in a tuple
'''

simple_foods = ('pizza', 'bread', 'beer', 'wine', 'liquor')

# Use a for loop to print each food the restaurant offers

[print(food.title()) for food in simple_foods]

# Try to modify one of the items, and make sure that Python rejects the change.

    # simple_foods[0] = 'water'

# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to
# print each of the items on the revised menu

simple_foods = ('pizza', 'chips', 'beer', 'wine', 'margarita')
print("\n")
[print(food.title()) for food in simple_foods]
