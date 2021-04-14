# Get the square of each number from 0 - 9:
def get_squares():
    squares = [x**2 for x in range(9)]

    print(squares)


# Get the square of each EVEN number:
# Includes if-statement
def get_even_squares():
    even_squares = [x**2 for x in range(9) if x % 2 == 0]

    print(even_squares)


# Get the square of each EVEN number
# Or, get x + 3
# Note, if/else statement must be moved before for loop
def get_even_square_3():
    even_square_3 = [x** 2 if x % 2 == 0 else x + 3 for x in range(9)]

    print(even_square_3)

get_even_square_3()