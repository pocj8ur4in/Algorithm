import sys
read = sys.stdin.readline

N = int(read())
L = list(map(int, read().split()))
P = list(map(int, read().split()))

C = 0
S = L[C] * P[C]

for i in range(1, N - 1):
    if L[i] * P [C] > L[i] * P[i]:
        C = i
    S += L[i] * P [C]

print(S)