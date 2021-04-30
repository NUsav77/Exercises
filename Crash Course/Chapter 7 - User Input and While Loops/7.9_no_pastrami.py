"""Using the list sandwich_orders from 7.8, make sure the sandwich 'pastrami' appears in the list at least three
times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of pastrami from sandwich_orders. Make sure no pastrami
sandwiches end up in finished sandwiches. """

sandwich_orders = [
    'pb&j',
    'tuna',
    'pastrami',
    'pastrami',
    'ham and cheese',
    'turkey breast',
    'pastrami',
]

finished_sandwiches = []

print('Unfortunately, we are out of pastrami. All pastrami orders will be cancelled.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making = sandwich_orders.pop()
    print(f'\nYour {making} sandwich is being made.')
    finished_sandwiches.append(making)

print('\nYour sandwiches are ready!')