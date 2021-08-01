# https://www.acmicpc.net/problem/3085
def calculate():
    temp_result = 0
    for i in range(n):
        current, count = table[i][0], 1
        for j in range(1, n):
            if table[i][j] == current:
                count += 1
            else:
                current, count = table[i][j], 1
            temp_result = max(temp_result, count)
    for i in range(n):
        current, count = table[0][i], 1
        for j in range(1, n):
            if table[j][i] == current:
                count += 1
            else:
                current, count = table[j][i], 1
            temp_result = max(temp_result, count)
    return temp_result


offsets = [(1, 0), (0, 1)]
n = int(input())
table = [list(input()) for _ in range(n)]
result = 0
for y in range(n):
    for x in range(n):
        cc = table[y][x]
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if ny < n and nx < n and table[ny][nx] != cc:
                nc = table[ny][nx]
                table[y][x], table[ny][nx] = nc, cc
                result = max(result, calculate())
                table[y][x], table[ny][nx] = cc, nc
    if result == n:
        break
print(result)



