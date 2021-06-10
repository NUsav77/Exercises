s = input()

alnum, alpha, digit, lower, upper = False, False, False, False, False

for char in s:
    if char.isalnum() == True:
        alnum = True
    if char.isalpha():
        alpha = True
    if char.isdigit():
        digit = True
    if char.islower():
        lower = True
    if char.isupper():
        upper = True

print(f'{alnum}\n{alpha}\n{digit}\n{lower}\n{upper}')