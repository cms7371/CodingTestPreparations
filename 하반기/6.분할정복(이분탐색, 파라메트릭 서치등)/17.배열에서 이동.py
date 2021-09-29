# https://www.acmicpc.net/problem/1981
from collections import deque


def explore(graph, low, high):
    if graph[0][0] < low or graph[0][0] > high:
        return False
    global N
    q = deque()
    q.append((0, 0))
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and (low <= graph[ny][nx] <= high):
                visited[ny][nx] = True
                q.append((ny, nx))
    return visited[-1][-1]




offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(set(comp for line in table for comp in line))
answer = 200
idx = 0
while True:
    l_inter, r_inter = 0, arr[-1] - arr[idx]
    is_explored = False
    while l_inter <= r_inter:
        mid = (l_inter + r_inter) // 2
        if explore(table, arr[idx], arr[idx] + mid):
            r_inter = mid - 1
            is_explored = True
        else:
            l_inter = mid + 1
    if is_explored:
        answer = min(answer, l_inter)
        idx += 1
    else:
        break
print(answer)