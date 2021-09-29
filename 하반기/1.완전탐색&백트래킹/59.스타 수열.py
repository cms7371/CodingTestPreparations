def solution(a):
    n = len(a)
    last = [-1] * n
    count = [0] * n
    for i in range(n):
        cur = a[i]
        if last[cur] < i - 1:
            last[cur] = i
            count[cur] += 1
        elif i < n - 1 and a[i + 1] != cur:
            last[cur] = i + 1
            count[cur] += 1
        else:
            last[cur] = i
    return max(count) * 2


print(solution([0, 1, 1, 2]))
