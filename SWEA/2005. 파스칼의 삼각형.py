N = int(input())

for n in range(1, N + 1):
    M = int(input())
    print("#" + str(n))

    S = []
    for m in range(1, M + 1):
        T = []

        if m == 1 or m == 2:
            T.append(1)
            if m == 2:
                T.append(1)
        else:
            T.append(1)
            for o in range(1, len(S)):
                T.append(S[-1][o - 1] + S[-1][o])
            T.append(1)

        for t in range(0, len(T) - 1):
            print(T[t], end=" ")
        print(T[-1])

        S.append(T)
