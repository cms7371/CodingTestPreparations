# https://www.acmicpc.net/problem/11660
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
parts = []
for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    parts.append((y1 - 1, x1 - 1, y2 - 1, x2 - 1))
sum_table = [line[:] for line in table]

for i in range(n):
    for j in range(1, n):
        sum_table[i][j] += sum_table[i][j - 1]
for i in range(1, n):
    for j in range(n):
        sum_table[i][j] += sum_table[i - 1][j]
for y1, x1, y2, x2 in parts:
    result = sum_table[y2][x2]
    if y1 > 0:
        result -= sum_table[y1 - 1][x2]
    if x1 > 0:
        result -= sum_table[y2][x1 - 1]
    if y1 > 0 and x1 > 0:
        result += sum_table[y1 - 1][x1 - 1]
    print(result)