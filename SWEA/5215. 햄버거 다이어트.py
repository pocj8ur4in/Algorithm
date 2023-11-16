def dfs(index, start, score, kcal):
    global M

    if score > M:
        M = score

    if index == N:
        return

    for i in range(start, N):
        if kcal + K[i] <= L:
            print(index + 1, i + 1, score + S[i], kcal + K[i])
            dfs(index + 1, i + 1, score + S[i], kcal + K[i])


T = int(input())

for t in range(1, T + 1):
    N, L = map(int, input().split(" "))
    S = []
    K = []

    for n in range(N):
        s, k = map(int, input().split(" "))
        S.append(s)
        K.append(k)

    M = 0
    dfs(0, 0, 0, 0)
    print(f"#{t} {M}")
