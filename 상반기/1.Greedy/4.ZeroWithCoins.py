# 11047번 동전 0 https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
index = n - 1
result = 0
while k != 0:
    if k // coins[index] != 0:
        result += k // coins[index]
        k = k % coins[index]
    index -= 1
print(result)
