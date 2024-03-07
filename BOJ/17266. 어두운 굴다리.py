import sys
import math
read = sys.stdin.readline

N = int(read())
M = int(read())
X = [*map(int, input().split())]
P = []

for i in range(0, M + 1):
    if i == 0:
        P.append(X[i])
    elif i == len(X):
        P.append(N - X[i - 1])
    else:
        P.append(math.ceil((X[i] - X[i - 1]) / 2))

print(max(P))
