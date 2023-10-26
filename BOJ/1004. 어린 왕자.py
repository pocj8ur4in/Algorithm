import sys
import math

read = sys.stdin.readline

T = int(read())

for t in range(T):
    x1, y1, x2, y2 = map(int, read().rstrip().split())

    N = int(read())
    L1 = []

    for n in range(N):
        L2 = list(map(int, read().rstrip().split()))
        L1.append(L2)

    ans = 0

    for n in range(N):
        cnt = 0

        for m in range(2):
            if m == 0:
                D = math.sqrt((x1 - L1[n][0]) ** 2 + (y1 - L1[n][1]) ** 2)
                if D < L1[n][2]:
                    cnt += 1
            else:
                D = math.sqrt((x2 - L1[n][0]) ** 2 + (y2 - L1[n][1]) ** 2)
                if D < L1[n][2]:
                    cnt += 1

        if cnt == 1:
            ans += 1

    print(ans)

