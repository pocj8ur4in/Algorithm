import sys
from itertools import combinations

read = sys.stdin.readline


N, S = map(int, read().split())
arr = list(map(int, read().split()))
result = 0

for i in range(1, N + 1):
    for j in combinations(arr, i):
        if sum(j) == S:
            result += 1

print(result)
