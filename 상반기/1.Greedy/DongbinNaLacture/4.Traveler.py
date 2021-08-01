# 문제 : 상하좌우
# 한 여행자가 NxN의 맵을 탐험합니다. 이때 여행자에게 상하죄우 움직임을 의미하는 U D R L의 명령을 주었을 때 최종 위치를 출력하시오

# 내 코드


def move(p, dx, dy):
    p[0] += dx
    p[1] += dy


N = int(input())
commands = input().split()

position = [1, 1]
for c in commands:
    next_position = [x for x in position]
    if c == "R":
        move(next_position, 0, 1)
    elif c == "U":
        move(next_position, -1, 0)
    elif c == "L":
        move(next_position, 0, -1)
    elif c == "D":
        move(next_position, 1, 0)
    if (next_position[0] <= N) & (next_position[0] >= 1) & (next_position[1] <= N) & (next_position[1] >= 1):
        position = next_position
    print(position[0], position[1])
print(position[0], position[1])


# 예시 코드
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
