# 13413번 오셀로 재배치 https://www.acmicpc.net/problem/13413
t = int(input())
result = []
for _ in range(t):
    n = int(input())
    init = input()
    obj = input()
    countW, countB = 0, 0
    for i in range(n):
        if init[i] == 'W' and obj[i] == 'B':
            countW += 1
        elif init[i] == 'B' and obj[i] == 'W':
            countB += 1
    result.append(max(countB, countW))
print("\n".join(map(str, result)))


