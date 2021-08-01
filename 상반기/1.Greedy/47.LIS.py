# 11053번 가장 긴 증가하는 부분 수열
# dp 테이블 또는 이진탐색으로 구현할 수 있음
# 첫번째 dp 테이블을 이용하여 구현
# n = int(input())
# seq = list(map(int, input().split()))
# dp = [1] * n
# result = 1
# for i in range(1, n):
#     max_dp = 0
#     for j in range(i):
#         if seq[j] < seq[i]:
#             max_dp = max(max_dp, dp[j])
#     dp[i] = max_dp + 1
#     result = max(dp[i], result)
# print(result)
# 두번째 이진 탐색을 이용한 구현
from bisect import bisect_left
n = int(input())
seq = list(map(int, input().split()))
result = []
for s in seq:
    index = bisect_left(result, s)
    if index == len(result):
        result.append(s)
    else:
        result[index] = s
print(len(result))



