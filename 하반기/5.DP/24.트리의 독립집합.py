# https://www.acmicpc.net/problem/2213
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(10e5))


def DFS(node, parent):
    dp[node][1] += weight[node]
    for child in path[node]:
        if child != parent:
            DFS(child, node)
            dp[node][0] += max(dp[child])
            dp[node][1] += dp[child][0]


def explore(node, parent, parent_selected):
    if parent_selected:
        for child in path[node]:
            if child != parent:
                explore(child, node, False)
    else:
        node_selected = max(dp[node]) == dp[node][1]
        if node_selected:
            result.append(node)
        for child in path[node]:
            if child != parent:
                explore(child, node, node_selected)


n = int(input())
weight = [0] + list(map(int, input().split()))
path = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().split())
    path[s].append(e)
    path[e].append(s)
dp = [[0, 0] for _ in range(n + 1)]
DFS(1, 0)
result = []
explore(1, 0, False)
result.sort()
print(max(dp[1]))
print(*result)

