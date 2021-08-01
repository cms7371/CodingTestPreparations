# https://www.acmicpc.net/problem/2468
from collections import defaultdict
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
height_dict = defaultdict(list)
for i in range(n):
    for j in range(n):
        height_dict[graph[i][j]].append((i, j))
heights = list(height_dict.keys())
heights.sort(reverse=True)
safe_area_map = [[False] * n for _ in range(n)]
result = 0
for h in heights:
    for y, x in height_dict[h]:
        safe_area_map[y][x] = True
    safe_area_num = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if safe_area_map[i][j] and not visited[i][j]:
                visited[i][j] = True
                safe_area_num += 1
                stack = [(i, j)]
                while stack:
                    y, x = stack.pop()
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n and safe_area_map[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
    result = max(result, safe_area_num)
print(result)


