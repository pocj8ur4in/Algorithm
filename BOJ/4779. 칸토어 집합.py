import sys
read = sys.stdin.readline


def cantor(string, index, number):
    if index == number:
        print(string)
    else:
        cantor(string + 3 ** index * " " + string, index + 1, number)


while True:
    try:
        cantor("-", 0, int(read()))
    except:
        break
