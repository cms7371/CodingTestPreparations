# https://www.acmicpc.net/problem/14002
n = int(input())
seq = list(map(int, input().split()))
dp = [1] * n
prev = [-1] * n
for i in range(n):  # 현재 탐색 중인 수
    for j in range(i):  # 비교하는 앞 쪽 수
        if seq[i] > seq[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j
m_dp = max(dp)
result = []
for i in range(n):
    if dp[i] == m_dp:
        result.append(seq[i])
        idx = prev[i]
        while idx != -1:
            result.append(seq[idx])
            idx = prev[idx]
        break
print(m_dp)
result.reverse()
print(*result)
