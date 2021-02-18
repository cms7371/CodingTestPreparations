# 5585번 거스름돈 https://www.acmicpc.net/problem/5585
n = int(input())
changes = 1000 - n
bills = [500, 100, 50, 10, 5, 1]
result = 0
for b in bills:
    result += changes // b
    changes %= b
print(result)


