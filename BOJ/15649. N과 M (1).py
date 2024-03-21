import sys
read = sys.stdin.readline


def bt(ars, cnt):
    if cnt == M:
        arr.append(ars)
    else:
        for i in range(1, N + 1):
            if i not in ars:
                tmp = ars.copy()
                tmp.append(i)
                bt(tmp, cnt + 1)


N, M = map(int, read().split())
arr = []

bt([], 0)

for i in arr:
    result = ""

    for j in i:
        result = result + str(j) + " "

    print(result)
