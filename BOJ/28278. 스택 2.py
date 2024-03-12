import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
stack = deque()

for i in range(N):
    command = read().split()
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        if stack.__len__() != 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(stack.__len__())
    elif command[0] == '4':
        if stack.__len__() == 0:
            print(1)
        else:
            print(0)
    elif command[0] == '5':
        if stack.__len__() != 0:
            print(stack[-1])
        else:
            print(-1)
