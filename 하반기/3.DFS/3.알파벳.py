# https://www.acmicpc.net/problem/1987
# 알파벳 스택을 유지하는 것으로는 시간초과가 남
# -> 비트마스트를 응용하듯 알파벳 방문표시


def DFS(y, x):
    global result, cnt
    cnt += 1
    result = max(result, cnt)
    alpha_occurred[ord(graph[y][x]) - 65] = True
    for dy, dx in offsets:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and not alpha_occurred[ord(graph[ny][nx]) - 65]:
            DFS(ny, nx)
    cnt -= 1
    alpha_occurred[ord(graph[y][x]) - 65] = False


offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
cnt = 0
alpha_occurred = [False] * 28
result = 0
DFS(0, 0)
print(result)
