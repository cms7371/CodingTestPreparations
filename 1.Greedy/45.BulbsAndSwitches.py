# 2138번 전구와 스위치 https://www.acmicpc.net/problem/2138
n = int(input())
original = list(map(int, list(input())))
after = list(map(int, list(input())))
def switch(be, af):
    c = 0
    for i in range(1, n):
        if be[i - 1] != af[i - 1]:
            c += 1
            be[i - 1] = 0 if be[i - 1] else 1
            be[i] = 0 if be[i] else 1
            if i < n - 1:
                be[i + 1] = 0 if be[i + 1] else 1
    return c
before = [i for i in original]
count = switch(before, after)
if before == after:
    print(count)
else:
    before = [i for i in original]
    before[0] = 0 if before[0] else 1
    before[1] = 0 if before[1] else 1
    count = switch(before, after) + 1
    if before == after:
        print(count)
    else:
        print(-1)





