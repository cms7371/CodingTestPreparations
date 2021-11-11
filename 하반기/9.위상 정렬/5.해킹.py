# https://www.acmicpc.net/problem/10282
from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    dependency = defaultdict(list)
    for _ in range(D):
        a, b, s = map(int, input().split())
        dependency[b].append((a, s))
    q = [(0, C)]
    visited = [False] * (N + 1)
    count = 0
    s_max = 0
    while q:
        s, cur = heappop(q)
        if visited[cur]:
            continue
        visited[cur] = True
        count += 1
        s_max = max(s, s_max)
        for _next, ss in dependency[cur]:
            if not visited[_next]:
                heappush(q, (s + ss, _next))
    print(count, s_max)
