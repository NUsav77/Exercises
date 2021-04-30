"""Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list
called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as 'I
made your tuna sandwich'. After all the sandwiches have been made, print a message listing each sandwich that was
made. """

sandwich_orders = [
    'pb&j',
    'tuna',
    'ham and cheese',
    'turkey breast',
]

finished_sandwiches = []

while sandwich_orders:
    making = sandwich_orders.pop()
    print(f'\nYour {making} sandwich is being made.')
    finished_sandwiches.append(making)

print('\nYour sandwiches are ready!')