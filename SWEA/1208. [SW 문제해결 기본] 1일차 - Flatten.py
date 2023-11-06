for t in range(1, 11):
    N = int(input())
    arr = list(map(int, input().rstrip().split(" ")))

    for n in range(0, N):
        m = arr.index(max(arr))
        n = arr.index(min(arr))

        arr[m] -= 1
        arr[n] += 1

    print("#" + str(t) + " " + str(max(arr) - min(arr)))
