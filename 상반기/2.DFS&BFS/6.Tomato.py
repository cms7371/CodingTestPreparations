# 7576번 토마토 https://www.acmicpc.net/problem/7576
# 양 옆에서 익는 경우 익히는 것과 인접한 토마토를 다음 익을 리스트에 넣는 것을 분리하지 않으면 반례가 생기게 됨 %%%중요
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
next_tomato = set()
def ripen(x, y):
    for o in offsets:
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            next_tomato.add((nx, ny))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ripen(i, j)
day = 0
while next_tomato:
    day += 1
    current = list(next_tomato)
    next_tomato = set()
    for t in current:
        graph[t[0]][t[1]] = 1
    for t in current:
        ripen(*t)
check = [0 in i for i in graph]
if any(check):
    print(-1)
else:
    print(day)

