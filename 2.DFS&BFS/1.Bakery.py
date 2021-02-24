# 3109번 빵집  https://www.acmicpc.net/problem/3109
# 두번째 시도 : 깊이 우선 탐색으로 시도? 왜 이게 그리디에 있는거야
# 다시 짜야함,..... 내일 도즈언
r, c = map(int, input().split())
graph = [[True if i == "." else False for i in list(input())] for _ in range(r)]
result = 0
for i in range(r):
    if graph[i][1]:
        x = 1
        y = i
        caches = [(y, x)]
        while x != c - 1:
            if y > 0 and graph[x + 1][y - 1]:
                x += 1
                y -= 1
            elif graph[x + 1][y]:
                x += 1
            elif y < r - 1 and graph[x + 1][y + 1]:
                x += 1
                y += 1
            else:
                break
            caches.append((y, x))
        if x == c - 1:
            result += 1
            for cache in caches:
                graph[cache[0]][cache[1]] = False
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




