for t in range(0, 10):
    N = int(input())
    arr = list(map(int, input().rstrip().split(" ")))
    ans = 0

    for m in range(2, N - 2):
        chk = arr[m - 2]

        if chk < arr[m - 1]:
            chk = arr[m - 1]
        if chk < arr[m + 1]:
            chk = arr[m + 1]
        if chk < arr[m + 2]:
            chk = arr[m + 2]

        if arr[m] > chk:
            ans += (arr[m] - chk)

    print("#" + str(t + 1) + " " + str(ans))
