import sys
import math
read = sys.stdin.readline

T = int(read())

for i in range(T):
    N = read().split()
    N = [int(n) for n in N]

    Z = math.sqrt((N[0] - N[3]) ** 2 + (N[1] - N[4]) ** 2)

    if Z == 0 and N[2] == 0 and N[5] == 0:
        print(1)
    elif N[2] + N[5] > Z > abs(N[2] - N[5]):  # 접점 2개
        print(2)
    elif (N[2] + N[5] == Z or abs(N[2] - N[5]) == Z) and Z != 0:  # 접점 1개
        print(1)
    elif N[2] + N[5] < Z or abs(N[2] - N[5]) > Z:  # 접점 0개
        print(0)
    elif Z == 0 and N[2] == N[5]:
        print(-1)