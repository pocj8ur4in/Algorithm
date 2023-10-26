import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
S = deque()

for i in range(N):
    C = read().split()
    if C[0] == "push":
        S.append(C[1])
    elif C[0] == "top":
        if len(S) == 0:
            print(-1)
        else:
            print(S[len(S) - 1])
    elif C[0] == "size":
        print(len(S))
    elif C[0] == "empty":
        if len(S) == 0:
            print(1)
        else:
            print(0)
    elif C[0] == "pop":
        if len(S) != 0:
            print(S[len(S) - 1])
            S.pop()
        else:
            print(-1)