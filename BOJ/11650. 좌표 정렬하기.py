import sys

read = sys.stdin.readline

N = int(read())
D = []

for n in range(N):
    x, y = map(int, read().split())

    D.append([x, y])

D.sort()

for n in range(len(D)):
    for m in range(len(D[n])):
        print(D[n][m], end=" ")
    print()

