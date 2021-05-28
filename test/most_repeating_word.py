def most_repeating_word(test):
    words = test.split()
    max_count = 0
    max_count_word = words[0]

    for word in words:
        for i in list(word):
            if word.count(i) > max_count:
                max_count = word.count(i)
                max_count_word = word

    return max_count_word

print(most_repeating_word('This is an elementary test example'))


test = 50
print(test)