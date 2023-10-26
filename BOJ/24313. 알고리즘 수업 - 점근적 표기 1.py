import sys
read = sys.stdin.readline

A, B = map(int, read().rstrip().split())
C = int(read())
N = int(read())

if A > 0 and C > 0:
    if A > C:
        print("0")
    elif A == C:
        if B > 0:
            print("0")
        else:
            print("1")
    else:
        if A * N + B <= C * N:
            print("1")
        else:
            print("0")
elif A > 0 >= C:
    print("0")
elif A == 0:
    if B <= C * N:
        print("1")
    else:
        print("0")
elif A < 0 < C:
    if A * N + B <= C * N:
        print("1")
    else:
        print("0")
elif A < 0 and C == 0:
    if A * N + B <= C * N:
        print("1")
    else:
        print("0")
elif A < 0 and C < 0:
    if A > C:
        print("0")
    elif A == C:
        if B > 0:
            print("0")
        else:
            print("1")
    else:
        if A * N + B <= C * N:
            print("1")
        else:
            print("0")