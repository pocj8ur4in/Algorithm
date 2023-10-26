import sys

read = sys.stdin.readline

x, y = map(int, read().split())
board = list()

for i in range(0, x):
    board.append(read().rstrip())

ans = -1

for i in range(0, x - 7):
    for j in range(0, y - 7):
        for k in range(0, 2):
            cnt = 0

            if k == 0:
                chk = "W"
            else:
                chk = "B"

            for a in range(0, 8):
                for b in range(0, 8):
                    if board[a + i][b + j] != chk:
                        cnt += 1

                    if chk == "W":
                        chk = "B"
                    else:
                        chk = "W"
                if chk == "W":
                    chk = "B"
                else:
                    chk = "W"

            if ans == -1:
                ans = cnt
            elif ans > cnt:
                ans = cnt

print(ans)