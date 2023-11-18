def find(temp):
    a = 1

    while 1:
        end = 0

        for n in range(1, a + 1):
            end += n

        if temp <= end:
            b = 1
            while temp != end:
                b += 1
                a -= 1
                end -= 1
            break

        a += 1

    return a, b


for T in range(1, int(input()) + 1):
    X, Y = map(int, input().rstrip().split(" "))

    x1, y1 = find(X)
    x2, y2 = find(Y)

    x3 = x1 + x2
    y3 = y1 + y2

    ans = 0

    for an in range(1, x3 + 1):
        ans += an

    for an in range(0, y3 - 1):
        ans += an + x3

    print("#" + str(T) + " " + str(ans))
