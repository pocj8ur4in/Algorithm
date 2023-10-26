import sys
read = sys.stdin.readline

N = int(read())
ans = N

for n in range(N):
    S = read().rstrip()
    L = []

    for s in S:
        if L.__contains__(s) == 0:
            L.append(s)
        elif L[-1] == s:
            continue
        else:
            ans -= 1
            break

print(ans)