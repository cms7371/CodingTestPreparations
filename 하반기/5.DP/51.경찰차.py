# https://www.acmicpc.net/problem/2618
import sys
input = sys.stdin.readline


def dist(sy, sx, ey, ex):
    return abs(sy - ey) + abs(sx - ex)


N = int(input())
W = int(input())
incident = [tuple(map(int, input().split())) for _ in range(W)]
dp = [[[10 ** 9, 0, 0] for _ in range(W + 1)] for _ in range(W + 1)]
dp[1][0][0] = dist(1, 1, *incident[0])
dp[0][1][0] = dist(N, N, *incident[0])
for i in range(2, W + 1):
    cur_d = dist(*incident[i - 1], *incident[i - 2])
    dp[i][0] = [cur_d + dp[i - 1][0][0], i - 1, 0]
    dp[0][i] = [cur_d + dp[0][i - 1][0], 0, i - 1]
for a in range(1, W + 1):
    for b in range(1, W + 1):
        if a == b:
            continue
        elif a > b:
            if a - b == 1:
                min_d = 10 ** 9
                min_i = 0
                for i in range(a - 1):
                    cur_d = (dist(*incident[i - 1], *incident[a - 1]) if i > 0 else dist(1, 1, *incident[a - 1])) + \
                            dp[i][b][0]
                    if cur_d < min_d:
                        min_d = cur_d
                        min_i = i
                dp[a][b] = [min_d, min_i, b]
            else:
                dp[a][b] = [dp[a - 1][b][0] + dist(*incident[a - 1], *incident[a - 2]), a - 1, b]
        else:
            if b - a == 1:
                min_d = 10 ** 9
                min_i = 0
                for i in range(b - 1):
                    cur_d = (dist(*incident[i - 1], *incident[b - 1]) if i > 0 else dist(N, N, *incident[b - 1])) + \
                            dp[a][i][0]
                    if cur_d < min_d:
                        min_d = cur_d
                        min_i = i
                dp[a][b] = [min_d, a, min_i]
            else:
                dp[a][b] = [dp[a][b - 1][0] + dist(*incident[b - 1], *incident[b - 2]), a, b - 1]
d, a, b = 10 ** 9, 0, 0
for i in range(W + 1):
    if dp[-1][i][0] < d:
        d, a, b = dp[-1][i][0], W, i
    if dp[i][-1][0] < d:
        d, a, b = dp[i][-1][0], i, W
stack = []
while a or b:
    _, na, nb = dp[a][b]
    if a == na:
        stack.append(2)
    else:
        stack.append(1)
    a, b = na, nb
print(d, *stack[::-1], sep='\n')
