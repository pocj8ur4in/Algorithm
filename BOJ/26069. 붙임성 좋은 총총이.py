import sys
read = sys.stdin.readline

N = int(read())
S = set()
S.add("ChongChong")

for n in range(N):
    X, Y = map(str, read().rstrip().split())
    if X in S and Y not in S:
        S.add(Y)
    elif X not in S and Y in S:
        S.add(X)

print(str(S.__len__()))