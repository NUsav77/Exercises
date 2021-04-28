'''
Use the third argument of the range() function to make a list of the odd numbers from
1 to 20. Use a for loop to print each number.
'''

for odd_num in range(1, 21, 2):
    print(odd_num)

# Using list comprehension:

[print(odd_num) for odd_num in range(1, 21, 2)]
