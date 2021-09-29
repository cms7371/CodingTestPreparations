# https://www.acmicpc.net/problem/2618
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def get_min_dist(a, b):
    if dp[a][b] != -1:
        return dp[a][b]
    elif a >= W + 1 or b >= W + 1:
        dp[a][b] = 0
        return 0
    _next = max(a, b) + 1
    case1 = get_min_dist(_next, b) + dist(pos[a], pos[_next])
    case2 = get_min_dist(a, _next) + dist(pos[b], pos[_next])
    dp[a][b] = min(case1, case2)
    return dp[a][b]


def track_back(a, b):
    if a >= W + 1 or b >= W + 1:
        return
    _next = max(a, b) + 1
    case1 = get_min_dist(_next, b) + dist(pos[a], pos[_next])
    case2 = get_min_dist(a, _next) + dist(pos[b], pos[_next])
    if case1 < case2:
        print(1)
        track_back(_next, b)
    else:
        print(2)
        track_back(a, _next)

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


N = int(input())
W = int(input())
pos = [(1, 1), (N, N)]
for _ in range(W):
    pos.append(tuple(map(int, input().split())))
dp = [[-1] * (W + 2) for _ in range(W + 2)]
print(get_min_dist(0, 1))
track_back(0, 1)