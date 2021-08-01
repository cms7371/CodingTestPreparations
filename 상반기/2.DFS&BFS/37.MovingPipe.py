# 17070번 파이프 옮기기1 https://www.acmicpc.net/problem/17070
def dfs(s, x, y):
    if x == n - 1 and y == n - 1:
        global result
        result += 1
    if s != 2 and y < n - 1 and graph[x][y + 1] == 0:
        dfs(0, x, y + 1)
    if x < n - 1 and y < n - 1 and graph[x][y + 1] == graph[x + 1][y] == graph[x + 1][y + 1] == 0:
        dfs(1, x + 1, y + 1)
    if s != 0 and x < n - 1 and not graph[x + 1][y]:
        dfs(2, x + 1, y)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
dfs(0, 0, 1)
print(result)






