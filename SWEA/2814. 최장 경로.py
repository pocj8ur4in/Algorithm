def dfs(v, cnt):
    global MAX

    if cnt > MAX:
        MAX = cnt

    for n in graph[v]:
        if not visited[n]:
            visited[n] = 1
            dfs(n, cnt + 1)
            visited[n] = 0


for t in range(1, int(input()) + 1):
    N, M = map(int, input().rstrip().split(" "))
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        X, Y = map(int, input().rstrip().split(" "))
        graph[X].append(Y)
        graph[Y].append(X)

    MAX = 0
    visited = [0] * (N + 1)

    for i in range(1, N + 1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print("#" + str(t) + " " + str(MAX))
