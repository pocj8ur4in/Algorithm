import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
Q = deque()

for i in range(N):
    C = read().split()
    if C[0] == 'push':
        Q.append(C[1])
    elif C[0] == 'pop':
        if len(Q) != 0:
            print(Q[0])
            Q.popleft()
        else:
            print(-1)
    elif C[0] == 'size':
        print(len(Q))
    elif C[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif C[0] == 'front':
        if len(Q) != 0:
            print(Q[0])
        else:
            print(-1)
    elif C[0] == 'back':
        if len(Q) != 0:
            print(Q[len(Q) - 1])
        else:
            print(-1)