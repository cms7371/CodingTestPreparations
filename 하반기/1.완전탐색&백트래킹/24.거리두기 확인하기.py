# https://programmers.co.kr/learn/courses/30/lessons/81302
# 2021 카카오 채용연계형 인턴십
from collections import deque
offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(places):
    answer = []
    for p in places:
        answer.append(explore(p))
    return answer


def explore(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                q = deque()
                q.append((i, j, 0, -1))
                while q:
                    y, x, dist, direction = q.popleft()
                    for idx in range(4):
                        if idx == (direction + 2) % 4:
                            continue
                        dy, dx = offset[idx]
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < 5 and 0 <= nx < 5:
                            if place[ny][nx] == "P":
                                return 0
                            elif place[ny][nx] == "O" and dist == 0:
                                q.append((ny, nx, 1, idx))
    return 1



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))



