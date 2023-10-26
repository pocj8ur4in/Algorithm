import sys
from collections import deque

read = sys.stdin.readline

K = int(read())
S = deque()

for i in range(K):
    R = int(read())
    if R == 0:
        S.pop()
    else:
        S.append(R)

print(sum(S))