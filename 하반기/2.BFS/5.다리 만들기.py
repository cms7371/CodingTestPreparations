# https://www.acmicpc.net/problem/2146
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 대륙을 구분하며 바운더리 검출 대륙별로 번호를 달리함
cnt_land_num = 2
result = 10e9  # 최소값이 될 결과
for i in range(n):
    for j in range(n):
        # 탐색하지 않은 땅인 경우 탐색하여 표시 후 바운더리 검출
        if graph[i][j] == 1:
            boundaries = []
            graph[i][j] = cnt_land_num
            q = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                is_appended = False
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n:
                        if graph[ny][nx] == 1:
                            graph[ny][nx] = cnt_land_num
                            q.append((ny, nx))
                        elif graph[ny][nx] == 0 and not is_appended:
                            boundaries.append((y, x))
                            is_appended = True
            # 바운더리에서 BFS를 하여 가장 가까운 대륙까지의 거리를 찾음
            for bound in boundaries:
                q = deque()
                q.append((*bound, 0))
                visited = [[False] * n for _ in range(n)]
                while q:
                    y, x, dist = q.popleft()
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n:
                            if graph[ny][nx] == 0:
                                if not visited[ny][nx]:
                                    visited[ny][nx] = True
                                    q.append((ny, nx, dist + 1))
                            # 다른 대륙을 만나면 탐색 종료
                            elif graph[ny][nx] != cnt_land_num:
                                result = min(result, dist)
                                q = False
                                break
        # 탐색 후 대륙 표시 번호 증가
        cnt_land_num += 1
print(result)
