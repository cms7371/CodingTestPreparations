# https://www.acmicpc.net/problem/2494
# dp[n][o]를 n번째가 o만큼 돌아갔을 때의 최솟값으로 정의하여 O(N * O)로 구할 수 있도록 함
INF = int(10e9)
N = int(input())
start, end = input(), input()
dp = [[[0, INF] for _ in range(10)] for _ in range(N)]
# 초기화
ss, es = int(start[0]), int(end[0])
if ss == es:
    dp[0][0][1] = 0
else:
    # 커지는 방향(다 같이 돌아가는 경우)
    p_offset = es - ss if es > ss else es - ss + 10
    # 작아지는 방향(혼자 돌아가는 경우)
    n_offset = ss - es if ss > es else ss - es + 10
    dp[0][p_offset][1] = p_offset
    dp[0][0][1] = n_offset
for n in range(1, N):
    for o in range(10):
        if dp[n - 1][o][1] != INF:
            c_digit = (int(start[n]) + o) % 10
            e_digit = int(end[n])
            if c_digit == e_digit:
                if dp[n][o][1] > dp[n - 1][o][1]:
                    dp[n][o][1], dp[n][o][0] = dp[n - 1][o][1], o
            else:
                # 왼쪽으로 돌리는 경우
                p_offset = e_digit - c_digit if e_digit > c_digit else e_digit - c_digit + 10
                no = (o + p_offset) % 10
                if dp[n - 1][o][1] + p_offset < dp[n][no][1]:
                    dp[n][no] = [o, dp[n - 1][o][1] + p_offset]
                # 오른쪽으로 돌리는 경우
                n_offset = c_digit - e_digit if c_digit > e_digit else c_digit - e_digit + 10
                if dp[n - 1][o][1] + n_offset < dp[n][o][1]:
                    dp[n][o] = [o, dp[n - 1][o][1] + n_offset]
val = INF
idx = -1
for o in range(10):
    if dp[-1][o][1] < val:
        idx, val = o, dp[-1][o][1]
print(val)
seq = []
for i in range(N - 1, 0, -1):
    prev_idx = dp[i][idx][0]
    prev_val = dp[i - 1][prev_idx][1]
    if idx == prev_idx:
        seq.append((i + 1, -(val - prev_val)))
    else:
        seq.append((i + 1, val - prev_val))
    idx, val = prev_idx, prev_val
seq.append((1, dp[0][idx][1] if idx != 0 else -dp[0][idx][1]))
seq.reverse()
for s in seq:
    print(*s)