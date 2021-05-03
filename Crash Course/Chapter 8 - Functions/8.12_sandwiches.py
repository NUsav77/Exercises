"""Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter
that collects as many items as the function call provides, and it should print a summary of the sandwich that's being
ordered. Call the function three times, using a different number of arguments each time. """


def make_sandwich(*toppings):
    print("Your sandwich topping(s) are: ")
    [print(f"\t{count+1}: {topping.title()}") for count, topping in enumerate(toppings)]


make_sandwich('pickles')
make_sandwich('lettuce', 'cheese')
make_sandwich('pineapples', 'salami', 'bacon')
