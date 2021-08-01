# https://www.acmicpc.net/problem/10819
# permutation을 이용한 간단한 풀이
from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
permute = permutations(arr)
result = 0
for p in permute:
    result = max(result, sum([abs(p[i] - p[i + 1]) for i in range(len(p) - 1)]))
print(result)
