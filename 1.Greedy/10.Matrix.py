# 1080번 행렬 https://www.acmicpc.net/problem/1080
# 넘나리 어려움.... 실패...
# 해설 https://m.blog.naver.com/PostView.nhn?blogId=pjok1122&logNo=221652193756&proxyReferer=https:%2F%2Fwww.google.com%2F
offsets = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1)]


def flip(x, y):
    for o in offsets:
        a[x + o[0]][y + o[1]] = 0 if a[x + o[0]][y + o[1]] else 1


n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]
count = 0
for i in range(0, n - 2):
    for j in range(0, m - 2):
        if a[i][j] != b[i][j]:
            count += 1
            flip(i + 1, j + 1)
for i in range(n):
    escape = False
    for j in range(m):
        if a[i][j] != b[i][j]:
            escape = True
            break
    if escape:
        break
if escape:
    print(-1)
else:
    print(count)

