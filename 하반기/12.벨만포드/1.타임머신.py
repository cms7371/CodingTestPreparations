# https://www.acmicpc.net/problem/11657
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
path = []
for _ in range(M):
    path.append(tuple(map(int, input().split())))
INF = 10 ** 9
dist = [INF] * (N + 1)
dist[1] = 0
isCycle = False
for i in range(N):
    for s, e, w in path:
        if dist[s] != INF and dist[s] + w < dist[e]:
            dist[e] = dist[s] + w
            if i == N - 1:
                isCycle = True
                break
if isCycle:
    print(-1)
else:
    for i in range(2, N + 1):
        print(dist[i] if dist[i] != INF else -1)
