import sys
read = sys.stdin.readline


M, N = map(int, read().rstrip().split())
data = [0] + [1] * (N - 1)

for num in range(2, N):
    for i in range(1, len(data) // num + 1):
        if i != 1 and data[i * num - 1] == 1:
            data[i * num - 1] = 0

for i in range(M - 1, len(data)):
    if data[i] == 1:
        print(i + 1)
