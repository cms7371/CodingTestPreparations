# 1700번 멀티탭 스케줄링 https://www.acmicpc.net/problem/1700
n, k = map(int, input().split())
gadgets = list(map(int, input().split()))
tab = []
result = 0
for i in range(len(gadgets)):
    if gadgets[i] in tab:
        continue
    elif len(tab) < n:
        tab.append(gadgets[i])

    else:
        weights = []
        for t in tab:
            try:
                next_position = gadgets[i+1:].index(t)
            except:
                next_position = 100
            weights.append(next_position)
        tab.pop(weights.index(max(weights)))
        tab.append(gadgets[i])
        result += 1
print(result)




