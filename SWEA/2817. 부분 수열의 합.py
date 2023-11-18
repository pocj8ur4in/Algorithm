from itertools import combinations

for t in range(1, int(input()) + 1):
    N, K = map(int, input().rstrip().split(" "))

    arr = list(map(int, input().rstrip().split(" ")))

    ans = 0
    for i in range(1, N + 1):
        for j in combinations(arr, i):
            if sum(j) == K:
                ans += 1

    print("#" + str(t) + " " + str(ans))
