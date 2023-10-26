import sys
read = sys.stdin.readline

T = int(read())

for i in range(T):
    S = str(read())
    S = S.replace("\n", "")
    while len(S) != 0:
        if "()" in S:
            S = S.replace("()", "")
        else:
            break

    if len(S) == 0:
        print("YES")
    else:
        print("NO")