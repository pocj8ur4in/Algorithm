import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
Q = deque()

for i in range(N):
    Q.append(i + 1)

for i in range(N - 1):
    Q.popleft()
    Q.append(Q[0])
    Q.popleft()

print(Q[0])