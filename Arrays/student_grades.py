if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        records += [name, score]

    # Sorts the scores and names from lowest to highest
    scores = sorted(records[1::2])
    names = sorted(records[::2])
    # second_lowest = names[1] + ' '

    for count, score in enumerate(scores):
        if score == scores[1]:
            # if names[count] in second_lowest:
            # continue
            print(names[count] + ' ')
