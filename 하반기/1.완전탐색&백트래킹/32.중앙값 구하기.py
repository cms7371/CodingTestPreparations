# https://www.acmicpc.net/problem/2696
from heapq import *
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N // 10 + 1):
        arr.extend(map(int, input().split()))
    result = [arr[0]]
    low_q = [-arr[0]]
    high_q = []
    for i in range(1, N):
        cur = arr[i]
        if cur > -low_q[0]:
            heappush(high_q, cur)
        else:
            heappush(low_q, -cur)
        if len(high_q) > len(low_q):
            heappush(low_q, -heappop(high_q))
        elif len(low_q) - len(high_q) > 1:
            heappush(high_q, -heappop(low_q))
        if i % 2 == 0:
            result.append(-low_q[0])
    print(len(result))
    for i in range(0, len(result), 10):
        print(*result[i:i + 10])
