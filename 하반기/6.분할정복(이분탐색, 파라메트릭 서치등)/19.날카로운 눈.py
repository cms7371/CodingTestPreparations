# https://www.acmicpc.net/problem/1637
from math import ceil
import sys
input = sys.stdin.readline


def count(start, end, first, last, interval):
    if start > last or end < first:
        return 0
    init_num = first if start <= first else first + ceil((start - first) / interval) * interval
    last_num = min(end, last)
    return (last_num - init_num) // interval + 1


N = int(input())
nums = []
for _ in range(N):
    nums.append(tuple(map(int, input().split())))
s, e = 1, 2 ** 31 - 1
while s != e:
    mid = (s + e) // 2
    low, high = 0, 0
    for a, c, b in nums:
        low += count(s, mid, a, c, b)
        high += count(mid + 1, e, a, c, b)
    if low % 2 == 1:
        e = mid
    elif high % 2 == 1:
        s = mid + 1
    else:
        break

if s != e:
    print("NOTHING")
else:
    print(s, sum(count(s, e, a, c, b) for a, c, b in nums))

