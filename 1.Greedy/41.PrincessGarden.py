# 2457번 공주님의 정원 -> 아직 성공 안함.....
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
