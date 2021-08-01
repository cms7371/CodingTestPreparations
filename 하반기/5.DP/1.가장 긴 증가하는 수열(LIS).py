# https://www.acmicpc.net/problem/11053
# 첫번째 방법: DP를 이용하여 O(N^2)으로 구하는 방법
n = int(input())
seq = list(map(int, input().split()))
dp = [1] * n
for i in range(n):  # 현재 탐색 중인 수
    for j in range(i):  # 비교하는 앞 쪽 수
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
# 두번째 방법: 이진 탐색을 이용하여 최장 증가 수열을 직접적으로 구하는 방법
from bisect import bisect_left
n = int(input())
seq = list(map(int, input().split()))
result = []
for i in range(n):
    idx = bisect_left(result, seq[i])
    if idx < len(result):
        result[idx] = seq[i]
    else:
        result.append(seq[i])
print(len(result))