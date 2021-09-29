# https://www.acmicpc.net/problem/7579


N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum_cost = sum(cost)
dp = [[-1] * (sum_cost + 1) for _ in range(N)]
dp[0][cost[0]] = memory[0]
for i in range(1, N):
    cur_c = cost[i]
    cur_m = memory[i]
    for c in range(sum_cost + 1):
        if dp[i - 1][c] != -1:
            dp[i][c] = max(dp[i][c], dp[i - 1][c])
            dp[i][c + cur_c] = max(dp[i][c + cur_c], dp[i - 1][c] + cur_m)
    dp[i][cur_c] = max(dp[i][cur_c], cur_m)
for c in range(sum_cost + 1):
    if dp[-1][c] >= M:
        print(c)
        break
print(*dp, sep='\n')