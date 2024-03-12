import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
stack1 = deque(map(int, read().split()))
stack2 = deque()

index = 1
for i in range(0, N):
    temp = stack1.popleft()
    if index == temp:
        index += 1
    else:
        stack2.append(temp)

    if stack2.__len__() != 0:
        if stack2[-1] == index:
            for j in range(stack2.__len__() - 1, -1, -1):
                if index == stack2[-1]:
                    stack2.pop()
                    index += 1
                else:
                    break

for i in range(0, len(stack2)):
    if i == index:
        index += 1
        stack2.pop()
    else:
        break

if stack1.__len__() == 0 and stack2.__len__() == 0:
    print('Nice')
else:
    print('Sad')
