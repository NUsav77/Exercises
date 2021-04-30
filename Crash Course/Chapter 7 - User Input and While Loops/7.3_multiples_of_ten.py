"""Ask the user for a number, and then report whether the number is a multiple of 10 or not."""

while True:
    mult_ten = input('Enter a number: ')
    if mult_ten == 'quit':
        break
    if int(mult_ten) % 10 == 0:
        print('This number is a multiple of ten.')
    else:
        print('This number is NOT a multiple of ten.')