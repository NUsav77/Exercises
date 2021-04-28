'''
All versions of foods.py iin this section have avoided
using for loops when printing to save space. Choose a version
of foods.py, and write two for loops to print each list of foods.
'''

my_foods = ['sinigang', 'kapoon', 'beef ribs', 'ribeye']
pas_foods = ['kapoon', 'rice', 'stir fry', 'noodles']

print(f"My favorite foods are:")
[print(food.title()) for food in my_foods]

print("\nPa's favorite foods are:")
[print(food.title()) for food in pas_foods]