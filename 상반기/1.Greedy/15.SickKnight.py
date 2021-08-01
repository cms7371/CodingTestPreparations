# 1783번 병든 나이트 https://www.acmicpc.net/problem/1783
n, m = map(int, input().split())
if n == 1:
    result = 1
elif n == 2:
    if m >= 7:
        result = 4
    elif m >= 5:
        result = 3
    elif m >= 3:
        result = 2
    else:
        result = 1
else:
    if m < 7:
        if m < 5:
            result = m
        else:
            result = 4
    else:
        result = m - 2
print(result)
