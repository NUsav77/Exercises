"""
You’re given a sequence of integers on a single line via standard input, each
separated by a single space. Print the maximum difference (in absolute value)
between any two numbers in the sequence on a single line on standard output.
Assumptions
1. Each number is separated by a single space.
2. The numbers can be positive, zero, or negative.
Example
Input:
1 9 2 -7 10 4 3
Output:
17
Explanation
The largest absolute difference between any two input numbers is |-7-10| = 17.
"""

s = str(input())
numbers = s.split()

temp2 = int(numbers[0])
maxdiff = 0

for num in numbers:
    temp = int(num)  # Convert str to int
    if temp2 - temp > maxdiff:
        maxdiff = temp2

print(maxdiff)
