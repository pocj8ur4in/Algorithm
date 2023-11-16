T = int(input())

for t in range(1, T + 1):
    N = int(input())

    arr = []
    for n in range(0, N):
        arr.append(input())

    ans = 0

    for n in range(0, N // 2 + 1):
        for m in range(N // 2 - n, N // 2 + n + 1):
            ans += int(arr[n][m])

    for n in range(N // 2 + 1, N):
        for m in range(n - N // 2, N - (n - N // 2)):
            ans += int(arr[n][m])

    print("#" + str(t) + " " + str(ans))

