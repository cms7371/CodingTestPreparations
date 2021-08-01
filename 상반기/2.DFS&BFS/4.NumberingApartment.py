# 2667번 단지번호붙이기 https://www.acmicpc.net/problem/2667
offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
result = []
def dfs(x, y):
    if 0 <= x < n and 0 <= y < n and graph[x][y] == 1:
        result[-1] += 1
        graph[x][y] = 0
        for o in offsets:
            dfs(x + o[0], y + o[1])
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(0)
            dfs(i, j)
result.sort()
print(len(result))
print("\n".join(map(str, result)))





