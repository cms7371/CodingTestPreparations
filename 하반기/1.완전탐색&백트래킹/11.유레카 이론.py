# https://www.acmicpc.net/problem/10448
t = int(input())
table = []
for i in range(1, 46):
    table.append((i * (i + 1)) // 2)
for _ in range(t):
    num = int(input())
    stop = False
    result = 0
    for i in range(len(table)):
        if stop: break
        for j in range(len(table)):
            if stop: break
            for k in range(len(table)):
                if table[i] + table[j] + table[k] == num:
                    result = 1
                    stop = True
                    break
    print(result)
