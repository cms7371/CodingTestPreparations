# https://www.acmicpc.net/problem/14003
from bisect import *
from heapq import *

N = int(input())
arr = list(map(int, input().split()))
LIS = []
idx_heap = []
for i in range(N):
    num = arr[i]
    bs = bisect_left(LIS, num)
    if bs == len(LIS):
        LIS.append(num)
        idx_heap.append([-i])
    else:
        LIS[bs] = num
        heappush(idx_heap[bs], -i)
print(len(LIS))
rev_idx = [-heappop(idx_heap[-1])]
for i in range(len(idx_heap) - 2, - 1, -1):
    while True:
        _next = -heappop(idx_heap[i])
        if _next < rev_idx[-1]:
            rev_idx.append(_next)
            break
for i in range(len(rev_idx) - 1, -1, -1):
    print(arr[rev_idx[i]], end=' ')