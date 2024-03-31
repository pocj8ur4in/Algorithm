import sys
read = sys.stdin.readline


def paper(tmp, chk1, chk2, chk3, chk4):
    global result1
    global result2
    if tmp[chk1[0]][chk1[1]] == tmp[chk2[0]][chk2[1]] == tmp[chk3[0]][chk3[1]] == tmp[chk4[0]][chk4[1]]:
        if tmp[chk1[0]][chk1[1]] == 0:
            result1 = result1 + 1
        else:
            result2 = result2 + 1
        return
    else:
        


X = int(read())

arr = []
for i in range(0, X):
    arr.append(list(map(int, read().split(" "))))
global result1
result1 = 0
global result2
result2 = 0

paper(arr, [0, 0], [0, X - 1], [X - 1, 0], [X - 1, X - 1])

print(result1)
print(result2)