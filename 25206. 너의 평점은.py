import sys
read = sys.stdin.readline

EntireSubject = 0.0
EntireSubjectNum = 0.0

for i in range(20):
    Subject = read().split()
    Subject[1] = float(Subject[1])

    if Subject[2] == "A+":
        EntireSubject += Subject[1] * 4.5
    elif Subject[2] == "A0":
        EntireSubject += Subject[1] * 4.0
    elif Subject[2] == "B+":
        EntireSubject += Subject[1] * 3.5
    elif Subject[2] == "B0":
        EntireSubject += Subject[1] * 3.0
    elif Subject[2] == "C+":
        EntireSubject += Subject[1] * 2.5
    elif Subject[2] == "C0":
        EntireSubject += Subject[1] * 2.0
    elif Subject[2] == "D+":
        EntireSubject += Subject[1] * 1.5
    elif Subject[2] == "D0":
        EntireSubject += Subject[1] * 1.0
    elif Subject[2] == "F":
        EntireSubject += Subject[1] * 0.0

    if Subject[2] != "P":
        EntireSubjectNum += Subject[1]

print(EntireSubject / EntireSubjectNum)