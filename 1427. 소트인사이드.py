import sys
read = sys.stdin.readline

N = read().rstrip()
L = []

for n in N:
    L.append(int(n))

L = list(reversed(sorted(L)))
L = ''.join(str(x) for x in L)

print(L)