"""Write a program that asks the user how many people are in their dinner group. If the answer is more than eight,
print a message saying they'll hav to wait for a table. Otherwise, report that their table is ready. """

party_count = int(input('How many people are in your party?: '))
if party_count > 8:
    print("Too bad, so sad")
else:
    print("Perfect! Your table is ready.")