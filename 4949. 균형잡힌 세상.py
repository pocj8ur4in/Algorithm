import sys
from collections import deque

read = sys.stdin.readline
S = read().rstrip()


while S != ".":
    D = deque()
    flag = 0

    for i in S:
        if i == ".":
            break
        elif i == "(":
            D.append("(")
        elif i == ")":
            if D.__len__() == 0:
                flag += 1
                break
            else:
                chk = D.pop()
                if chk == "(":
                    continue
                else:
                    flag += 1
                break
        elif i == "[":
            D.append("[")
        elif i == "]":
            if D.__len__() == 0:
                flag += 1
                break
            else:
                chk = D.pop()
                if chk == "[":
                    continue
                else:
                    flag += 1
                    break

    if flag == 1 or D.__len__() != 0:
        print("no")
    else:
        print("yes")

    S = read().rstrip()