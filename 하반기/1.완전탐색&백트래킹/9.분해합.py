# https://www.acmicpc.net/problem/2231
n = int(input())
digits = len(str(n))
result = 0
for i in range(max(0, n - 9 * digits), n):
    nums = list(map(int, str(i)))
    if i + sum(nums) == n:
        result = i
        break
print(result)
