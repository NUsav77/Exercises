'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string. The input string can be assumed
to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''


def duplicate_count(text):
    holder = {}
    final_count = 0

    # Creates a dict for each char in text.
    # They char is the key
    # The count of the char is the value
    for char in text.lower():
        if char not in holder.keys():
            holder[char] = 1
        elif char in holder.keys():
            holder[char] += 1

    for char, count in holder.items():
        if count > 1:
            final_count += 1

    return final_count


string1 = 'abcde'
string2 = 'aabbcde'
string3 = 'aabBcde'

print(duplicate_count(string3))
