'''
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker
indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them
to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or,
if anyone has bribed more than two people, print Too chaotic.

Example
q = [1, 2, 3, 4, 5, 6, 7, 8]
If person 5 bribes person 4, the queue will look like this: [1, 2, 3, 5, 4, 6, 7, 8]. Only  bribe is required. Print 1.

q = [4, 1, 2, 3]
Person 4 had to bribe 3 people to get to the current position. Print Too chaotic.

FUNCTION DESCRIPTION:

Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):
    int q[n]: the positions of the people after all bribes

Returns
    No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than
    people.

Input Format
The first line contains an integer t, the number of test cases.
Each of the next t pairs of lines are as follows:
- The first line contains an integer t, the number of people in the queue
- The second line has n space-separated integers describing the final state of the queue.

Constraints
- 1 <= t <= 10
- 1 <= n <= 10**5

Subtasks
For 60% score 1 <= n <= 10**3
for 100% score 1 <= n <= 10**5

Sample Input

STDIN       Function
-----       --------
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]

Sample Output
-------------
3
Too chaotic

Explanation

Test Case 1
The initial state:
RIDE: 1 -- 2 -- 3 -- 4 -- 5
    After person 5 moves one position ahead by bribing person 4:
RIDE: 1 -- 2 -- 3 -- 5 -- 4
    Now person 5 moves another position ahead by bribing person 3:
RIDE: 1 -- 2 -- 5 -- 3 -- 4
    And person 2 moves one position ahead by bribing person 1:
RIDE: 2 -- 1 -- 5 -- 3 -- 4
    So the final state is 2, 1, 5, 3, 4 after three bribing operations.

Test Case 2
No person can bribe more than two people, yet it appears person  has done so. It is not possible to achieve the input state.
'''

# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.

t = 1
n = 5
queue = [5, 1, 2, 3, 4]


def minimumBribes(q):
    # Number of moves initialized to 0
    moves = 0

    q = [P - 1 for P in q]  # Takes each number in list q and subtracts 1 to make things easier to understand
    print(f'q is {q}')  # Prints numbers within list q
    for i, P in enumerate(q):   # Creates a position i for each value of P using enumerate()
        if P - i > 2:   # Checks if any person P is more than two ahead of its original position
                        # If it is, automatically goes to "Too chaotic" and ends.
            print("Too chaotic")
            return
        # From here on out, we don't care if P has moved forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is ahead of P.  P's original position is the value
        # of P. Anyone who bribed P cannot get to higher than one position in front if P's original position,
        # so we need to look from one position in front of P's original position to one in front of P's
        # current position, and see how many of those positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1, which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an index less than zero, replace P-1 with max(P-1,0)
        for j in range(max(P - 1, 0), i):
            if q[j] > P:
                moves += 1
    print(moves)


minimumBribes(queue)

'''
if __name__ == '__main__':
    t = int(input('Enter number of test cases: '))

    for t_itr in range(t):
        n = int(input('Enter number of people in queue: '))
        q = list(map(int, input('Enter space-separated queue order (e.g. 1 4 2 3 5): ').rstrip().split()))
        minimumBribes(q)
'''
