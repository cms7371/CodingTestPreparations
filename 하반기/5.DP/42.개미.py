# https://www.acmicpc.net/problem/14942
from collections import deque
import sys
input = sys.stdin.readline


def log2(a):
    out = 0
    while a > 1:
        out += 1
        a //= 2
    return out


N = int(input())
e = [int(input()) for _ in range(N)]
path = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    path[a].append((b, c))
    path[b].append((a, c))
dp = [[None] * (N + 1) for _ in range(log2(N) + 1)]
q = deque()
dp[0][1] = (1, 0)  # 다음 노드, 거리
q.append((0, 1))  # parent, 현재 노드로 큐에 넣음
while q:
    parent, cur = q.popleft()
    for node, cost in path[cur]:
        if node != parent:
            dp[0][node] = (cur, cost)
            q.append((cur, node))

for i in range(1, log2(N) + 1):
    for j in range(1, N + 1):
        n_node, cost = dp[i - 1][j]
        nn_node, n_cost = dp[i - 1][n_node]
        n_cost += cost
        dp[i][j] = (nn_node, n_cost)
for i in range(1, N + 1):
    cur_e = e[i - 1]
    node = i
    j = len(dp) - 1
    while node != 1 and j >= 0:
        if dp[j][node][1] <= cur_e:
            cur_e -= dp[j][node][1]
            node = dp[j][node][0]
        j -= 1
    print(node)