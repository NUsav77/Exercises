def swap_case(s):
    update = ''
    for char in s:
        if char.islower:
            update += char.swapcase()
        elif char.isupper:
            update += char.swapcase()
        else:
            update += char
    return update

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
