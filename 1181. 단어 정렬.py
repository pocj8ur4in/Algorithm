import sys

read = sys.stdin.readline

N = int(read())
words = []

for n in range(N):
    words.append(read().rstrip())

for k in range(0, 51):
    chks = set()

    for word in range(len(words)):
        if len(words[word]) == k:
            chks.add(words[word])

    chks = list(chks)
    chks.sort()

    for chk in chks:
        print(chk)