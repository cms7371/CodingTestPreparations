# https://www.acmicpc.net/problem/1516
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
time = [0] * (n + 1)
path = [[] for _ in range(n + 1)]
tech = [set() for _ in range(n + 1)]
in_degree = [0] * (n + 1)
for i in range(1, n + 1):
    seq = list(map(int, input().split()))
    time[i] = seq[0]
    for j in range(1, len(seq) - 1):
        path[seq[j]].append(i)
        in_degree[i] += 1
q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    for _next in path[now]:
        tech[_next].add(now)
        in_degree[_next] -= 1
        if in_degree[_next] == 0:
            time[_next] += max([time[i] for i in tech[_next]])
            q.append(_next)
print(*time[1:], sep='\n')
