# https://www.acmicpc.net/problem/1655
from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
h_heap, l_heap = [], []
for _ in range(N):
    cur = int(input())
    if not l_heap or cur < -l_heap[0]:
        heappush(l_heap, -cur)
    else:
        heappush(h_heap, cur)
    if len(h_heap) > len(l_heap):
        heappush(l_heap, -heappop(h_heap))
    if len(l_heap) - len(h_heap) > 1:
        heappush(h_heap, -heappop(l_heap))
    print(-l_heap[0])

