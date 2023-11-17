for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split(" "))
    arr = sorted(list(map(int, input().split())))
    time = 0

    ans = "Possible"
    for n in range(0, N):
        if arr[n] // M * K - n <= 0:
            ans = "Impossible"

    print("#" + str(t) + " " + ans)
