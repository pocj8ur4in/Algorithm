import sys


def euc(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a


read = sys.stdin.readline
x, y = map(int, read().rstrip().split())
z = euc(x, y)

if z == 1:
    print(str(x * y))
else:
    print(str(int(x * y / z)))