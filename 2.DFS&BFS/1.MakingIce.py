# 문제 : 음료수 얼려먹기 https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3&t=228s
# 44분
from collections import deque


# 나의 풀이 -> 버그가 있음
n, m = map(int, input().split())
ice_map = []
for i in range(n):
    ice_map.append(list(map(bool, (map(int, input())))))
visit_map = [[False] * m for _ in range(n)]
ice_queue = deque()
block_queue = deque()
count = 0
isCurrentIceChecked = False
visit_map[0][0] = True
if ice_map[0][0]:
    block_queue.append((0, 0))
else:
    ice_queue.append((0, 0))
    count += 1
    isCurrentIceChecked = True
for l in ice_map:
    print(l)

while ice_queue or block_queue:
    if ice_queue:
        x, y = ice_queue.popleft()
        if not isCurrentIceChecked:
            count += 1
            isCurrentIceChecked = True
            print("count increase on ", x, y)
    else:
        x, y = block_queue.popleft()
        if isCurrentIceChecked:
            isCurrentIceChecked = False
    print(x, y)

    visit_map[x][y] = True
    if x < n - 1:
        if not visit_map[x + 1][y]:
            if ice_map[x + 1][y]:
                block_queue.append((x + 1, y))
            else:
                ice_queue.append((x + 1, y))
    if y < m - 1:
        if not visit_map[x][y + 1]:
            if ice_map[x][y + 1]:
                block_queue.append((x, y + 1))
            else:
                ice_queue.append((x, y + 1))
print(count)


# 예시 코드
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
