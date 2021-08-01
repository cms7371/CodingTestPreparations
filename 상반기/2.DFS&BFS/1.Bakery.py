# 3109번 빵집  https://www.acmicpc.net/problem/3109
# 세번째 시도 : 완전 탐색으로 거름망 같이 각 경우를 쳐내보는 것?

# 두번째 시도 : 깊이 우선 탐색 -> 시간 초과.... O(C^3)의 시간 복잡도를 가지게 됨
# 세번째 시도 -> 스택을 이용하지 않고 방문하면 모두 False로 바꿔버림 -> 어차피 안되는 경로라면 다음에 다시 접근해도
# 안되기 때문에 중복 접근을 막아버림
r, c = map(int, input().split())
graph = [[True if i == "." else False for i in list(input())] for _ in range(r)]
result = 0
def bfs(x, y):
    graph[x][y] = False
    global result, stop
    if y < c - 2:
        if x > 0 and graph[x - 1][y + 1] and not stop:
            bfs(x - 1, y + 1)
        if graph[x][y + 1] and not stop:
            bfs(x, y + 1)
        if x < r - 1 and graph[x + 1][y + 1] and not stop:
            bfs(x + 1, y + 1)
    elif y == c - 2:
        result += 1
        stop = True
for i in range(r):
    if graph[i][1]:
        stop = False
        stack = []
        bfs(i, 1)
print(result)


# 첫번째 시도 : 두 열을 비교해서 연결될 수 있는 경우를 모두 찾은 후 그 중 최솟값을 반환한다
# 실패 -> 두 열만 비교하면 앞쪽에서 이어질 수 없는 경우를 거르지 못
r, c = map(int, input().split())
graph = [[True if i == "." else False for i in list(input())] for _ in range(r)]
results = []
for i in range(1, c - 2):
    l_now = [graph[j][i] for j in range(r)]
    l_next = [graph[j][i + 1] for j in range(r)]
    count = 0
    for j in range(r):
        if l_now[j]:
            if j > 0 and l_next[j - 1]:
                count += 1
                l_next[j - 1] = False
            elif l_next[j]:
                count += 1
                l_next[j] = False
            elif j < r - 1 and l_next[j + 1]:
                count += 1
                l_next[j + 1] = False
    results.append(count)
print(min(results))




