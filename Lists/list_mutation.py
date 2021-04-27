if __name__ == '__main__':
    N = int(input())
    list = []

    for _ in range(N):
        line = input().split()
        if line[0] == 'insert':
            list.insert(int(line[1]), int(line[2]))
        if line[0] == 'remove':
            for rem in list:
                list.pop(int(line[1]))
    print(list)
