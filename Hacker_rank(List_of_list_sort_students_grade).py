if __name__ == '__main__':
    L1 = []
    L2 = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        L1.append([name, score])

    L1.sort(key=lambda x: x[1])
    i = 1
    L1_duplicates = []
    for i in range(len(L1)):
        L1_duplicates.append(L1[i][1])

    var1 = L1_duplicates[0]
    count = 1

    for i in range(1, len(L1_duplicates)):
        if (L1_duplicates[i] == var1):
            count += 1
    for i in range(count, len(L1)):
        j = i + 1
        if (j < len(L1) and L1[i][1] == L1[j][1]):
            L2.append(L1[i][0])
            L2.append(L1[j][0])

    L2.sort()

    if len(L2) <= 1:
        print(L1[1][0])
    else:
        for i in L2:
            print(i)