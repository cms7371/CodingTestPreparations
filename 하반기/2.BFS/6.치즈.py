# https://www.acmicpc.net/problem/2638
from collections import defaultdict, deque  # 넣어놓지 않은 값에 대해 자동으로 구조물을 정할 수 있는 자료구조
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 치즈의 수를 카운트(끝을 알기 위해)
cheese_num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cheese_num += 1
time = 0
# 바깥 공기를 BFS하고 접촉하는 치즈 카운트
while cheese_num > 0:
    melt_cheese = defaultdict(int)  # 선언에는 값이 아닌 람다나 함수를 넘겨야함. int를 넘기게 되면 int()에서 0을 반환함
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                elif graph[ny][nx] == 1:
                    melt_cheese[(ny, nx)] += 1
    # 시간 증가, 치즈 제거, 치즈 남아있는지 확인
    for y, x in melt_cheese:
        if melt_cheese[(y, x)] >= 2:
            graph[y][x] = 0
            cheese_num -= 1
    time += 1
print(time)

