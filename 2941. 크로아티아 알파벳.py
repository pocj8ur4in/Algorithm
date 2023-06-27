import sys
read = sys.stdin.readline

C = list(read().rstrip())
ans = 0
c = 0

while c < len(C):
    if C[c] == "c" and c + 1 != len(C):
        if C[c + 1] == "=" or C[c + 1] == "-":
            ans += 1
            c += 1
        else:
            ans += 1
    elif C[c] == "d" and c + 1 != len(C):
        if C[c + 1] == "z" and c + 2 != len(C):
            if C[c + 2] == "=":
                ans += 1
                c += 2
            else:
                ans += 1
        elif C[c + 1] == "-":
            ans += 1
            c += 1
        else:
            ans += 1
    elif (C[c] == "l" or C[c] == "n") and c + 1 != len(C):
        if C[c + 1] == "j":
            ans += 1
            c += 1
        else:
            ans += 1
    elif (C[c] == "s" or C[c] == "z") and c + 1 != len(C):
        if C[c + 1] == "=":
            ans += 1
            c += 1
        else:
            ans += 1
    else:
        ans += 1
    c += 1

print(ans)