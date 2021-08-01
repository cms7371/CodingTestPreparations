# https://www.acmicpc.net/problem/2805
from functools import reduce


N, M = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, max(arr)
while l <= r:
    mid = (l + r) // 2
    cur_m = reduce(lambda acc, cur: acc + cur - mid if cur > mid else acc, arr, 0)
    if cur_m >= M:
        l = mid + 1
    else:
        r = mid - 1
print(r)