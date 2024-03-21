import sys
from collections import deque

read = sys.stdin.readline

T = int(read())

for i in range(0, T):
    n, m = map(int, read().split())
    queue = deque(map(int, read().split()))

    count = 0
    while queue:
        maxi = max(queue)
        front = queue.popleft()
        m -= 1

        if maxi == front:
            count += 1
            if m < 0:
                print(count)
                break

        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1
