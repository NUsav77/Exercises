'''
Make a list of the multiples of 3 from 2 to 30. Use a for loops to print the numbers
in your list
'''

mult_of_three = []
for num in range(3, 31, 3):
    mult_of_three.append(num)

for num in mult_of_three:
    print(num)

# Using list comprehension

[print(num) for num in range(3, 31, 3)]