def count_substring(string, sub_string):
    total = 0

    for count, i in enumerate(string):
        if string[count:count + len(sub_string)] == sub_string:
            total += 1

    print(total)

count_substring('I am an Indian, by birth.', 'Birth')