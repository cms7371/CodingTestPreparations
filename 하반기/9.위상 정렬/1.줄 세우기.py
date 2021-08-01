# https://www.acmicpc.net/problem/2252
# 굳이 set을 쓸 이유가 없었음
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
path = [set() for _ in range(n + 1)]
in_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    path[a].add(b)
    in_degree[b] += 1
q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
result = []
while q:
    now = q.popleft()
    result.append(now)
    for _next in path[now]:
        in_degree[_next] -= 1
        if in_degree[_next] == 0:
            q.append(_next)
print(*result)