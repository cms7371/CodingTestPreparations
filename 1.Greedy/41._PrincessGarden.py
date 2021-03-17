# 2457번 공주님의 정원 https://www.acmicpc.net/problem/2457
# 복습 풀이
n = int(input())
flowers = []
for _ in range(n):
    s1, e1, s2, e2 = map(int, input().split())
    flowers.append((s1 * 100 + e1, s2 * 100 + e2))
flowers.sort(key=lambda x: (x[0], -x[1]))
result = [flowers[0]]
for i in range(n):
    if result[-1][1] < flowers[i][1]:
        if len(result) > 1 and result[-2][1] >= flowers[i][0]:
            result[-1] = flowers[i]
        else:
            result.append(flowers[i])
    if result[-1][1] > 1200:
        break
if result[0][0] <= 301 and result[-1][1] >= 1200:
    print(len(result))
    print(result)
else:
    print(0)


# 첫 풀이
n = int(input())
data = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if not (a == 12 or c < 3):
        data.append((max(301, 100 * a + b), 100 * c + d))
data.sort(reverse=True, key=lambda x: x[1])
data.sort(key=lambda x: x[0])
if data[0][0] > 301:
    print(0)
else:
    result = [data[0]]
    for i in range(1, n):
        if result[-1][1] >= 1200:
            break
        if data[i][1] <= result[-1][1]:
            continue
        elif result[-1][1] < data[i][0]:
            break
        else:
            if len(result) > 1 and result[-2][1] >= data[i][0]:
                result.pop()
            result.append(data[i])
    if result[-1][1] >= 1200:
        print(len(result))
    else:
        print(0)
