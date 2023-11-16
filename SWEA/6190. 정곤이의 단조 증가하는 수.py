T = int(input())

for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().rstrip().split()))

    ans = -1
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if i == j:
                continue
            else:
                X = A[i] * A[j]
                X = str(X)

                chk = False
                for x in range(0, len(X) - 1):
                    if X[x] > X[x + 1]:
                        chk = True
                        break
                if not chk:
                    if ans < int(X):
                        ans = int(X)

    print("#" + str(t) + " " + str(ans))
