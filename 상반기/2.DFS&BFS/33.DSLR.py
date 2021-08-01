# 9019번 DSLR https://www.acmicpc.net/problem/9019

from collections import deque
def d(x):
    y = x * 2
    y %= 10000
    return y, "D"
def s(x):
    y = x - 1
    if y < 0:
        y = 9999
    return y, "S"
def l(x):
    y = x * 10
    if y >= 10000:
        y %= 10000
        y += x // 1000
    return y, "L"
def r(x):
    y = x // 10
    y += (x % 10) * 1000
    return y, "R"


t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append(tuple(map(int, input().split())))
output = []
for start, end in test_cases:
    q = deque()
    q.append((start, ""))
    visited = [False] * 10000
    visited[start] = True
    while q:
        cnum, command = q.popleft()
        for nnum, c in (d(cnum), s(cnum), l(cnum), r(cnum)):
            if nnum == end:
                output.append(command + c)
                q = False
                break
            elif not visited[nnum]:
                q.append((nnum, command + c))
                visited[nnum] = True
print("\n".join(output))



