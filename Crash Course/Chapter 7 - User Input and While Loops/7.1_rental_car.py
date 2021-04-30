"""Write a program that asks the user what kind of rental car they would like. Print a message about that car,
such as 'let me see if I can find you a Subaru'. """

print("Welcome to Savage Rentals!")
car = input("What kind of car are you looking for? ")
print(f'Good choice! Let me see if I can find a {car.title()}')