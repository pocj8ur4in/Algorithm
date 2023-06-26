import sys
read = sys.stdin.readline

N = int(read())
S = 0

for i in range(N):
    S += 1

    while True:
        if "666" in str(S):
            break
        else:
            S += 1

print(S)