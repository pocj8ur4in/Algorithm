import sys

read = sys.stdin.readline

N, M = map(int, read().split())
pocket = dict()

for i in range(1, N + 1):
    pocket[i] = read().rstrip()

convert_pocket = {v:k for k,v in pocket.items()}

for i in range(0, M):
    search = read().rstrip()

    if search[0].isdigit():
        print(pocket.get(int(search)))
    else:
        print(convert_pocket.get(search))
