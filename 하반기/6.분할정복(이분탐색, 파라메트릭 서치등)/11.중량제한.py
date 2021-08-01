# https://www.acmicpc.net/problem/1939
# BFS를 함 이때 노드를 기준으로 보기 보다는 전파되는 것을 기준으로 봄
# 초기값을 10e9로 하며 탐색을 진행하되 전파 값이 다리에의해 줄어들면 도착 노드를 기록함. 그리고 도착 노드에서는 그 전파값을 저장
# 만약 방문한 노드를 다시 방문하게 됐는데 전파값이 더 크다? 그러면 그 노드의 전파값을 업데이트
# 예상 시간 복잡도 O(N + M)
""" 결론적으로 큐에 너무 많은 것들이 들어가서 터져버림. 이분탐색과 BFS를 같이하는 방법을 이용해야함"""
# 개선한 버전
from collections import deque
import sys


input = sys.stdin.readline
INF = int(10e10)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
candidates = set()
for _ in range(M):
    a, b, limit = map(int, input().split())
    graph[a].append((b, limit))
    graph[b].append((a, limit))
    candidates.add(limit)
start, end = map(int, input().split())
candidates = list(candidates)
candidates.sort()
l, r = 0, len(candidates) - 1  # l = mid + 1, r = mid r은 같을 때까지 포함
while l <= r:
    mid = (l + r) // 2
    current = candidates[mid]
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque()
    q.append(start)
    while q and not visited[end]:
        now = q.popleft()
        for _next, _limit in graph[now]:
            if _limit >= current and not visited[_next]:
                q.append(_next)
                visited[_next] = True
    if visited[end]:
        l = mid + 1
    else:
        r = mid - 1


print(candidates[r])



