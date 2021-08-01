# 13549번 숨바꼭질3 https://www.acmicpc.net/problem/13549
# 세번째 시도 deque를 이용해서 제곱수는 앞에 앞 뒤 이동은 뒤로?
from collections import deque
n, k = map(int, input().split())
visited = [-1] * 100001
q = deque()
visited[n] = 0
q.append(n)
while visited[k] == -1:
    now = q.popleft()
    if now * 2 <= 100000 and visited[now * 2] == -1:
        visited[now * 2] = visited[now]
        q.appendleft(now * 2)
    if now + 1 <= 100000 and visited[now + 1] == -1:
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)
    if now - 1 >= 0 and visited[now - 1] == -1:
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)
print(visited[k])

# 두번째 시도 BFS로 시도하되 현재 위치가 K보다 큰 경우를 모두 제외해버림 -> 성공
n, k = map(int, input().split())
visited = [False] * 100001
result = abs(k - n)
position = [n]
visited[n] = True
time = 0
while time < result:
    for p in position[:]:
        while True:
            np = p * 2
            if np <= 100000 and not visited[np] and abs(k - p) > abs(k - np):
                visited[np] = True
                result = min(result, time + abs(k - np))
                if np < k:
                    position.append(np)
                p = np
            else:
                break
    time += 1
    next_position = []
    for p in position[:]:
        for np in (p + 1, p - 1):
            if 0 <= np <= 100000 and not visited[np]:
                visited[np] = True
                result = min(result, time + abs(k - np))
                if np < k:
                    next_position.append(np)
    position = next_position
print(result)







# 첫번째 시도 BFS로 모두 탐색 -> 당연히 시간 초과
n, k = map(int, input().split())
visited = [False] * 100001
init = n
current_position = []
while init <= 100000:
    visited[init] = True
    current_position.append(init)
    init *= 2
time = 0
found = True if k in current_position else False
while not found:
    time += 1
    next_position = []
    for p in current_position:
        for np in (p + 1, p - 1):
            if 0 <= np <= 100000 and not visited[np]:
                visited[np] = True
                next_position.append(np)
    for p in next_position[:]:
        pp = p * 2
        while pp <= 100000:
            if not visited[pp]:
                visited[pp] = True
                next_position.append(pp)
            pp *= 2
    current_position = next_position
    found = True if k in current_position else False
print(time)
