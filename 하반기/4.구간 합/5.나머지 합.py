# https://www.acmicpc.net/problem/10986
from collections import Counter
from math import comb
N, M = map(int, input().split())
arr = list(map(int, input().split()))
p_sum = [0]
for i in range(N):
    p_sum.append((p_sum[-1] + arr[i]) % M)
counter = Counter(p_sum)
result = 0
for num in counter:
    result += comb(counter[num], 2)
print(result)