import sys
read = sys.stdin.readline

N = int(read())
X = int(N / 5)
ans = -1

for x in range(X + 1):
    M = N
    cnt = x
    M -= x * 5

    if M % 3 == 0:
        while M != 0:
            cnt += 1
            M -= 3

    if ans == -1 and M == 0:
        ans = cnt
    elif ans > cnt and M == 0:
        ans = cnt

print(ans)