# 문제 : 왕실의 나이트
# 8x8 체스판 위에 한 점에 나이트의 위치가 주어졌을 경우 이동할 수 있는 경우의 수를 구하여라
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
# ord('a') = 97임
coord = input()
y, x = ord(coord[0]) - 96, int(coord[1])
count = 0
for i in range(len(dx)):
    nx, ny = x + dx[i], y + dy[i]
    if 0 < nx < 9 and 0 < ny < 9:
        count += 1
print(count)

# 예시 코드
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a')) + 1)
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1
print(result)
