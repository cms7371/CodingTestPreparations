# https://www.acmicpc.net/problem/16946
from collections import deque
import sys
input = sys.stdin.readline
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]
cluster_weight = [0]
wall = []
for i in range(R):
    for j in range(C):
        if table[i][j] == '1':
            wall.append((i, j))
            table[i][j] = 0
        elif table[i][j] == '0':
            table[i][j] = len(cluster_weight)
            cur_weight = 1
            q = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < R and 0 <= nx < C and table[ny][nx] == '0':
                        cur_weight += 1
                        table[ny][nx] = len(cluster_weight)
                        q.append((ny, nx))
            cluster_weight.append(cur_weight)
answer = [[0] * C for _ in range(R)]
for y, x in wall:
    adj_cluster = set()
    for dy, dx in offsets:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C:
            adj_cluster.add(table[ny][nx])
    answer[y][x] += 1 + sum(cluster_weight[idx] for idx in adj_cluster)
    answer[y][x] %= 10
print(*("".join(map(str, line)) for line in answer), sep='\n')
