# 5427번 불 https://www.acmicpc.net/problem/5427
# 첫 시도 -> 메모리 초과 -> 방문 처리를 하지 않은 것이 문제였음
import sys
input = sys.stdin.readline
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())
cases = []
for _ in range(t):
    m, n = map(int, input().split())
    graph = [list(input()) for _ in range(n)]
    cases.append((n, m, graph))
output = []
for n, m, graph in cases:
    current_p = []
    fire = []
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "*":
                fire.append((i, j))
            elif graph[i][j] == "@":
                current_p.append((i, j))
                visited[i][j] = True
    result = -1
    time = 1
    while current_p:
        next_fire = []
        for x, y in fire:
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "#" and graph[nx][ny] != "*":
                    graph[nx][ny] = "*"
                    next_fire.append((nx, ny))
        next_p = []
        for x, y in current_p:
            if x in (0, n - 1) or y in (0, m - 1):
                result = time
                next_p = False
                break
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == "." and not visited[nx][ny]:
                    next_p.append((nx, ny))
                    visited[nx][ny] = True
        time += 1
        fire = next_fire
        current_p = next_p
    output.append("IMPOSSIBLE" if result == -1 else str(result))
print("\n".join(output))

