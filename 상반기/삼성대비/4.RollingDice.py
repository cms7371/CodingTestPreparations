# 14499번 주사위 굴리기 https://www.acmicpc.net/problem/14499
import sys
def roll(direction):
    global dice
    if direction == 0:
        new_dice = [dice[i] for i in (3, 1, 0, 5, 4, 2)]
    elif direction == 1:
        new_dice = [dice[i] for i in (2, 1, 5, 0, 4, 3)]
    elif direction == 2:
        new_dice = [dice[i] for i in (4, 0, 2, 3, 5, 1)]
    else:
        new_dice = [dice[i] for i in (1, 5, 2, 3, 0, 4)]
    dice = new_dice

input = sys.stdin.readline
offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 동서북남
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = list(map(lambda a: int(a) - 1, input().split()))
dice = [0] * 6
for c in command:
    nx, ny = x + offsets[c][0], y + offsets[c][1]
    if 0 <= nx < n and 0 <= ny < m:
        roll(c)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[5]
        else:
            dice[5] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])