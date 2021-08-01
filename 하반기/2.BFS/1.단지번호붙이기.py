# https://www.acmicpc.net/problem/2667
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
block_count = 0
block_sizes = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            block_count += 1
            cnt_block_size = 1
            graph[i][j] = 0
            q = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
                        graph[ny][nx] = 0
                        cnt_block_size += 1
                        q.append((ny, nx))
            block_sizes.append(cnt_block_size)
block_sizes.sort()
print(block_count, *block_sizes, sep="\n")



