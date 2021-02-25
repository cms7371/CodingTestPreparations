# 2810번 컵홀더 https://www.acmicpc.net/problem/2810
n = int(input())
s = input()
i = 0
holder = 1
while i < n:
    if s[i] == "S":
        i += 1
    else:
        i += 2
    holder += 1
print(min(holder, n))

