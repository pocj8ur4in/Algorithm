for i in range(1, 11):
    ins = int(input())
    arr = []
    for a in range(0, 100):
        arr.append(list(map(int, input().rstrip().split(" "))))

    m = 0
    for a in range(0, len(arr)):
        t = 0
        for b in range(0, len(arr[a])):
            t += arr[a][b]
        if m < t:
            m = t

    for a in range(0, len(arr)):
        t = 0
        for b in range(0, len(arr[a])):
            t += arr[b][a]
        if m < t:
            m = t

    t = 0
    for a in range(0, len(arr)):
        t += arr[a][a]
    if m < t:
        m = t

    t = 0
    for a in range(0, len(arr)):
        t += arr[99 - a][99 - a]
    if m < t:
        m = t

    print("#" + str(i) + " " + str(m))

