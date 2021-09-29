# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
INF = 10 ** 9


def solution(board):
    answer = 0
    N = len(board)
    visited_h = [[INF] * N for _ in range(N)]
    visited_v = [[INF] * N for _ in range(N)]
    visited_h[0][0], visited_h[0][1] = 0, 0
    q = deque()
    q.append((0, 1, 0, True))
    while q and visited_h[-1][-1] == INF and visited_v[-1][-1] == INF:
        y, x, t, is_horizontal = q.popleft()
        if is_horizontal:
            if x < N - 1 and not board[y][x + 1] and t + 1 < visited_h[y][x + 1]:  # 오른쪽으로 이동
                visited_h[y][x + 1] = t + 1
                q.append((y, x + 1, t + 1, True))
            if x > 1 and not board[y][x - 2] and t + 1 < visited_h[y][x - 1]:  # 왼쪽
                visited_h[y][x - 1] = t + 1
                q.append((y, x - 1, t + 1, True))
            if y < N - 1 and not board[y + 1][x - 1] and not board[y + 1][x]:  # 아래가 비어있을 때
                if t + 1 < visited_h[y + 1][x]:  # 그대로 아래로 이동하는 경우
                    visited_h[y + 1][x] = t + 1
                    q.append((y + 1, x, t + 1, True))
                if t + 1 < visited_v[y + 1][x - 1]:  # 시계방향으로 돌려서 내려가는 경우
                    visited_v[y + 1][x - 1] = t + 1
                    q.append((y + 1, x - 1, t + 1, False))
                if t + 1 < visited_v[y + 1][x]:  # 반시계 방향으로 돌려서 내려가는 경우
                    visited_v[y + 1][x] = t + 1
                    q.append((y + 1, x, t + 1, False))
            if y > 0 and not board[y - 1][x - 1] and not board[y - 1][x]:  # 위에가 비어있는 경우
                if t + 1 < visited_h[y - 1][x]:  # 그대로 위로 올리는 경우
                    visited_h[y - 1][x] = t + 1
                    q.append((y - 1, x, t + 1, True))
                if t + 1 < visited_v[y][x - 1]:  # 반시계로 돌려서 수직이 되는 경우
                    visited_v[y][x - 1] = t + 1
                    q.append((y, x - 1, t + 1, False))
                if t + 1 < visited_v[y][x]:
                    visited_v[y][x] = t + 1
                    q.append((y, x, t + 1, False))
        else:  # 수직인 경우
            if y > 1 and not board[y - 2][x] and t + 1 < visited_v[y - 1][x]:  # 위로 이동
                visited_v[y - 1][x] = t + 1
                q.append((y - 1, x, t + 1, False))
            if y < N - 1 and not board[y + 1][x] and t + 1 < visited_v[y + 1][x]:  # 아래로 이동
                visited_v[y + 1][x] = t + 1
                q.append((y + 1, x, t + 1, False))
            if x > 0 and not board[y - 1][x - 1] and not board[y][x - 1]:  # 왼쪽이 비어있는 경우
                if t + 1 < visited_v[y][x - 1]:  # 그대로 이동하는 경우
                    visited_v[y][x - 1] = t + 1
                    q.append((y, x - 1, t + 1, False))
                if t + 1 < visited_h[y - 1][x]:  # 시계방향으로 돌리는 경우(위쪽으로)
                    visited_h[y - 1][x] = t + 1
                    q.append((y - 1, x, t + 1, True))
                if t + 1 < visited_h[y][x]:  # 반시계로 돌아(아래쪽)
                    visited_h[y][x] = t + 1
                    q.append((y, x, t + 1, True))
            if x < N - 1 and not board[y - 1][x + 1] and not board[y][x + 1]:  # 오른쪽이 비어있는 경우
                if t + 1 < visited_v[y][x + 1]:
                    visited_v[y][x + 1] = t + 1
                    q.append((y, x + 1, t + 1, False))
                if t + 1 < visited_h[y - 1][x + 1]:
                    visited_h[y - 1][x + 1] = t + 1
                    q.append((y - 1, x + 1, t + 1, True))
                if t + 1 < visited_h[y][x + 1]:
                    visited_h[y][x + 1] = t + 1
                    q.append((y, x + 1, t + 1, True))
    return min(visited_h[-1][-1], visited_v[-1][-1])


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))