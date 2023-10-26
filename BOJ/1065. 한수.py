import sys
read = sys.stdin.readline

N = int(read())
ans = 0

for i in range(1, N + 1):
    if i < 100:
        ans += 1
    elif 100 <= i < 1000:
        a = i // 100
        b = (i % 100) // 10
        c = i % 10

        if c - b == b - a:
            ans += 1

print(ans)
