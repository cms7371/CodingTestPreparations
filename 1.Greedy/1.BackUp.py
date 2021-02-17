# 문제 : 1150번 백업 https://www.acmicpc.net/problem/1150
# 솔루션 https://latter2005.tistory.com/34
import heapq


n, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]

q = []
for i in range(n-1):
    q.append(tuple([graph[i + 1] - graph[i], i, i + 1]))
while len(q) == k:
    now = heapq.heappop(q)
    dis, a, b = now



