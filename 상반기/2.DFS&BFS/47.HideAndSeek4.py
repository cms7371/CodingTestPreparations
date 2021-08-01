# 13913번 숨바꼭질 4 https://www.acmicpc.net/problem/13913
from collections import deque
s, d = map(int, input().split())
visited = [False] * 100001
q = deque()
q.append((s, 0))
visited[s] = (s, 0)
while q:
    now, dist = q.popleft()
    if now == d:
        break
    for n in (now + 1, now - 1, now * 2):
        if 0 <= n <= 100000 and not visited[n]:
            visited[n] = (now, dist + 1)
            q.append((n, dist + 1))
path = [d]
while True:
    current = path[-1]
    n = visited[current][0]
    if current == n:
        break
    else:
        path.append(n)
path.reverse()
print(visited[d][1])
print(" ".join(map(str, path)))