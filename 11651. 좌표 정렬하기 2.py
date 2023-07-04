import sys

read = sys.stdin.readline

N = int(read())
D = []

for n in range(N):
    x, y = map(int, read().split())

    D.append([y, x])

D.sort()

for n in range(len(D)):
    for m in range(1, -1, -1):
        print(D[n][m], end=" ")
    print()

