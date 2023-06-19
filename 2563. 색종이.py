import sys
read = sys.stdin.readline

M = [[0 for c in range(100)] for r in range(100)]

N = int(read())

for i in range(N):
    X, Y = map(int, read().split())
    for j in range(X - 1, X + 9):
        for k in range(Y - 1, Y + 9):
            M[j][k] = 1

S = 0

for j in range(100):
    for k in range(100):
        S += M[j][k]

print(S)