# https://www.acmicpc.net/problem/2075
from heapq import *
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
heapify(arr)
for _ in range(N - 1):
    n_comps = map(int, input().split())
    for comp in n_comps:
        heappush(arr, comp)
        heappop(arr)
print(heappop(arr))
