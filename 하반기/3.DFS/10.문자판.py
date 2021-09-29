# https://www.acmicpc.net/problem/2186
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def explore(y, x, idx):
    global N, M, K, L, word
    if idx not in visited[y][x]:
        if idx == L - 1:
            visited[y][x][idx] = 1
        else:
            temp = 0
            for dy, dx in offsets:
                for k in range(1, K + 1):
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= ny < N and 0 <= nx < M and table[ny][nx] == word[idx + 1]:
                        temp += explore(ny, nx, idx + 1)
            visited[y][x][idx] = temp
    return visited[y][x][idx]



N, M, K = map(int, input().split())
table = [list(input()) for _ in range(N)]
word = input()
L = len(word)
visited = [[{} for _ in range(M)] for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == word[0]:
            answer += explore(i, j, 0)
print(answer)
