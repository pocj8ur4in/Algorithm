import sys
from collections import deque
read = sys.stdin.readline

N, K = map(int, read().split())
D1 = deque()

print("<", end="")

for n in range(N):
    D1.append(n + 1)

for n in range(N):
    for k in range(K):
        D1.append(D1.popleft())

    if n != N - 1:
        print(str(D1.pop()) + ", ", end="")
    else:
        print(str(D1.pop()), end="")

print(">")