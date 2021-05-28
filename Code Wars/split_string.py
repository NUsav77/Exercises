'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''


def solution(s):
    n = 2
    pairs = []
    for char in range(0, len(s), n):
        pairs.append(s[char:char + n])
        if len(pairs[-1]) == 1:
            pairs[-1] += '_'
    return pairs


print(solution('abcdefg'))
