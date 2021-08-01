# https://www.acmicpc.net/problem/14165
# dp를 이해하는 데 너무 오래 걸림
N, M, K = map(int, input().split())
fj = list(map(int, input().split()))
fj.sort()
fp = list(map(int, input().split()))
fp.sort()
dp = [[1] * (M + 1) for _ in range(N + 1)]
# k번째 temp[i][j]는 'fj[i] fp[j] 원소를 매칭 시켰을 때' 가능한 경우의 수로
# 이는 dp[i][j](한 인덱스 밀려서 i - 1, j - 1까지 가능한 경우의 수)에 fj[i]와 fp[j]를 매칭시키는 경우가 됨
# 이를 누적합 하면 구하는 경우의 수가 나옴옴dp = [[1] * (N + 1) for _ in range(M + 1)]
for _ in range(K):
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if fj[i] > fp[j]:
                temp[i][j] = dp[i][j]
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = (temp[i][j] + dp[i + 1][j] + dp[i][j + 1] - dp[i][j]) % 1000000009
print(dp[-1][-1])