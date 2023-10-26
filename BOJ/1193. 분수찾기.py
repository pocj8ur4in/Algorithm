import sys
read = sys.stdin.readline

X = int(read())

x = 1
y = 1
z = 1

for i in range(X - 1):
    if x == 1 and y % 2 == 1:
        y += 1
        z = 0
    elif y == 1 and x % 2 == 0:
        x += 1
        z = 1
    elif z == 0:
        x += 1
        y -= 1
    elif z == 1:
        x -= 1
        y += 1

# 출력
print(str(x) + "/" + str(y))