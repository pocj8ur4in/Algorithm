import sys
read = sys.stdin.readline

N = int(read())
SET = set()
ans = 0

for n in range(N):
    S = read().rstrip()
    if S != "ENTER":
        if S not in SET:
            SET.add(S)
            ans += 1
    else:
        SET.clear()

print(str(ans))