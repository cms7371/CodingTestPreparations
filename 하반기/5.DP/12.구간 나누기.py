# https://www.acmicpc.net/problem/2228
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
pSum = [0]
for i in range(n):
    pSum.append(pSum[-1] + nums[i])
dp = [[0] * (n + 1) for _ in range(m + 1)]
# dp 각 라인의 초기값을 세팅해 줌
dp[1][1] = nums[0]
for i in range(2, m + 1):
    dp[i][2 * i - 1] = dp[i - 1][2 * i - 3] + nums[2 * i - 2]
for i in range(1, m + 1):
    for j in range(2 * i, n + 1):  # 1, 3, 5번째 자리의 다음(2, 4, 6)부터 시작함
        dp[i][j] = dp[i][j - 1]  # 현재 값을 선택하지 않는 경우 최댓값은 이전 값을 그대로 따라가고
        for k in range(2 * i - 3, j - 1):  # 현재 값을 선택하면 현재값을 포함하는 새로운 구간을 만들어서 최댓값 선택해 줌
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + pSum[j] - pSum[k + 1])
print(dp[-1][-1])


# 성공은 했지만 O(N^4)으로 과한 연산이 필요함 -> 문제는 dp의 값이 선택했을 때의 최댓값으로 k번째 이전 값을 사용하며
# l구간을 다시 계산함에 있음 -> 테이블의 값을 그때까지의 최댓값으로 선택하면 개선할 수 있음
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
pSum = [0]
for i in range(n):
    pSum.append(pSum[-1] + nums[i])
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    if i >= 2:
        dp[i][2 * i - 1] = dp[i - 1][2 * i - 3] + nums[2 * i - 2]
    else:
        dp[i][2 * i - 1] = nums[2 * i - 2]
    for j in range(2 * i, n + 1):
        dp[i][j] = dp[i][j - 1] + nums[j - 1]
        for k in range(2 * i - 3, j - 1):  # k는 i - 1개의 구간을 고른 경우에서 k번째까지 선택한 것을 이용한 경우
            for l in range(k + 1, j):
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + pSum[j] - pSum[l])
print(max(dp[-1][2 * m - 1:]))
