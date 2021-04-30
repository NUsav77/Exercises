"""A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3,
the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket. """

party_count = 0
total_price = 0

while True:
    party_count = int(input('How many people in your party: '))
    for _ in range(1, party_count+1):
        age = int(input(f'\nWhat is the age of person {_}: '))
        if age < 3:
            total_price += 0
            print('This person is free.')
        elif age < 12:
            total_price += 10
            print('This person is $10.00.')
        elif age >= 12:
            total_price += 15
            print('This person is $15.00.')
        if _ == party_count:
            print(f"\nYour total price is {total_price}.00.")
            break
        print(f"\nYour price so far is {total_price}.00.")