# https://www.acmicpc.net/problem/11048
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            table[i][j] += table[i][j - 1]
        elif j == 0:
            table[i][j] += table[i - 1][j]
        else:
            table[i][j] += max(table[i - 1][j - 1], table[i - 1][j], table[i][j - 1])
print(table[-1][-1])