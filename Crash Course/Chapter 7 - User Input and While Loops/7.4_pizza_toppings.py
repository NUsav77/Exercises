"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they
enter each topping, print a message saying you'll add that topping to their pizza. """

toppings = []

while True:
    topping = input("Enter a topping you'd like to add to your pizza. \n(If you're done, enter 'quit'): ")

    if topping == 'quit':
        print('Your pizza will have the following toppings:')
        [print(f"\t{t.title()}") for t in toppings]
        break
    else:
        toppings.append(topping)
