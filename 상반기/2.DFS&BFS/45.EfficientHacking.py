# 1325번 효율적인 해킹 https://www.acmicpc.net/problem/1325
# 첫 시도 -> 간단하게 연결관계를 나타내고 완전 탐색 -> 시간이 문제가 될 수도? -> 역시나 시간 초과로 실패 -> sys input 사용, 코드 최적화로 성공
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
result = [0] * (n + 1)
m_result = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True
    v = 0
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        v += 1
        for next_node in graph[now]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
    result[i] = v
    m_result = max(m_result, v)
for i in range(1, n + 1):
    if result[i] == m_result:
        print(i, end=" ")



