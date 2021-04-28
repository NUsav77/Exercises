'''
Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts
at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million
numbers.
'''

one_to_million = []

for num in range(1, 1_000_001):
    one_to_million.append(num)

print(f"The minimum value in my list is {min(one_to_million)}")

print(f"The maximum value in my list is {max(one_to_million)}")

print(f"The sum of all the numbers in my list is {sum(one_to_million)}")