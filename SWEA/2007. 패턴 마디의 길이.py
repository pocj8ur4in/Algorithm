N = int(input())

for i in range(0, N):
    S = input()

    for j in range(1, 11):
        K = S[0]

        for k in range(1, j):
            K += S[k]

        A = ""
        for k in range(0, 30 // j):
            A += K

        for k in range(0, 30 % j):
            A += K[k]

        if A == S.rstrip():
            print("#" + str(i + 1) + " " + str(j))
            break
