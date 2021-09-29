# https://www.acmicpc.net/problem/2666
from collections import defaultdict

N = int(input())
i1, i2 = map(int, input().split())
if i1 > i2:
    i1, i2 = i2, i1
M = int(input())
order = [int(input()) for _ in range(M)]
dp = {(i1, i2): 0}
for no in order:
    ndp = defaultdict(lambda: 10 ** 9)
    for key, val in dp.items():
        o1, o2 = key
        if no <= o1:
            ndp[(no, o2)] = min(ndp[(no, o2)], val + (o1 - no))
        elif no >= o2:
            ndp[(o1, no)] = min(ndp[(o1, no)], val + (no - o2))
        else:
            ndp[(o1, no)] = min(ndp[(o1, no)], val + (o2 - no))
            ndp[(no, o2)] = min(ndp[(no, o2)], val + (no - o1))
    dp = ndp
print(min(dp.values()))