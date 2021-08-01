# 1758번 알바생 강호 https://www.acmicpc.net/problem/1758
n = int(input())
customers = [int(input()) for _ in range(n)]
customers.sort(reverse=True)
result, i = 0, 0
while i < n:
    if i < customers[i]:
        result += customers[i] - i
        i += 1
    else:
        break
print(result)
