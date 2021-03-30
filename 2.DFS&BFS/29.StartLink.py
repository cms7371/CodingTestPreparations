# 5014번 스타트링크 https://www.acmicpc.net/problem/5014
from collections import deque
total, start, destination, up, down = map(int, input().split())
if start == destination:
    print(0)
else:
    visited = [False] * (total + 1)
    q = deque()
    q.append((start, 0))
    stop = False
    result = 0
    while q and not stop:
        current, count = q.popleft()
        for next_f in (current + up, current - down):
            if 0 < next_f <= total and not visited[next_f]:
                if next_f == destination:
                    result = count + 1
                    stop = True
                    break
                else:
                    visited[next_f] = True
                    q.append((next_f, count + 1))
    print("use the stairs" if result == 0 else result)





