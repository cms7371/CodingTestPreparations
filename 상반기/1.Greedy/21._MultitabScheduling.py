# 1700번 멀티탭 스케줄링 https://www.acmicpc.net/problem/1700
n, k = map(int, input().split())
schedule = list(map(int, input().split()))
tap = []
result = 0
for i in range(k):
    if schedule[i] in tap:
        continue
    elif len(tap) < n:
        tap.append(schedule[i])
    else:
        crit = []
        for t in tap:
            j = i + 1
            while j < k:
                if schedule[j] == t:
                    break
                else:
                    j += 1
            crit.append((j, t))
        crit.sort()
        tap.remove(crit[-1][1])
        tap.append(schedule[i])
        result += 1
print(result)


# 첫 풀이
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




