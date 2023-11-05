T = int(input())

for i in range(1, T + 1):
    N = int(input())
    S = list(map(int, input().rstrip().split()))

    M = S[-1]
    A = 0
    for j in range(N - 2, -1, -1):
        if M >= S[j]:
            A += M - S[j]
        else:
            M = S[j]
            continue
    print("#" + str(i) + " " + str(A))
