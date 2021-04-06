# 5567번 결혼식 https://www.acmicpc.net/problem/5567
# set을 이용한 두번째 풀이 -> 
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = set(graph[1])
for f in graph[1]:
    result = result.union(graph[f])
print(len(result) - 1)
# 벨만 포드 응용한 방법 첫번째 풀이
n = int(input())
m = int(input())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
visited = [False] * (n + 1)
visited[1] = True
for j in range(2, n + 1):
    if graph[1][j]:
        visited[j] = True
        for k in range(2, n + 1):
            if graph[j][k]:
                visited[k] = True
print(visited.count(True) - 1)
