import sys
read = sys.stdin.readline

N = int(read())
L = list()

for n in range(N):
    L.append(int(read()))

L.sort()

for n in range(N):
    print(L[n])