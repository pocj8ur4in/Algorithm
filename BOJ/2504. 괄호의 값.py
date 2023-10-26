import re
import sys
from collections import deque

read = sys.stdin.readline

S = deque(str(read()))

while S.__len__() != 2:
    S = ''.join(S)
    if '()' in S:
        S = S.replace('()', '2,')
    elif '[]' in S:
        S = S.replace('[]', '3,')
    else:
        if ',' in S:
            if ',)' in S:
                p = re.compile("([0-9]+,)")
                rel = p.findall(S)
                S = re.sub("([0-9]+,)", str(int(rel[0]) * 2), S)
                print(S)



    S = deque(S)

print(S[0])

# (()[[]])([])
# (2,[3,])(3,)
# (2,9,)6
# (11)6
# 22,6
# 28
