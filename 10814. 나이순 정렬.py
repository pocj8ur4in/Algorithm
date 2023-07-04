import sys

read = sys.stdin.readline

N = int(read())
words = []

for n in range(N):
    age, name = map(str, read().rstrip().split())
    words.append([n, int(age), name])

for i in range(1, 201):
    chks = []

    for word in words:
        if word[1] == i:
            chks.append(word[0])

    chks.sort()

    for chk in chks:
        print(words[chk][1], end=" ")
        print(words[chk][2])