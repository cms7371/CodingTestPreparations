# https://www.acmicpc.net/problem/2631
from bisect import *


N = int(input())
arr = [int(input()) for _ in range(N)]
result = []
for num in arr:
    idx = bisect_left(result, num)
    if idx == len(result):
        result.append(num)
    else:
        result[idx] = num
print(N - len(result))