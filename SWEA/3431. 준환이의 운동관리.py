for T in range(1, int(input()) + 1):
    L, U, X = map(int, input().rstrip().split(" "))

    if X < L:
        print("#" + str(T) + " " + str(L - X))
    elif L < X < U:
        print("#" + str(T) + " " + "0")
    else:
        print("#" + str(T) + " " + "-1")
