# 11399번 ATM https://www.acmicpc.net/problem/11399

n = int(input())
customers = list(map(int, input().split()))
customers.sort()
for i in range(1, n):
    customers[i] += customers[i - 1]
print(sum(customers))
