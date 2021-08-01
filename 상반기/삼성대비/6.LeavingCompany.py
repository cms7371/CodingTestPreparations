# 14501번 퇴사 https://www.acmicpc.net/problem/14501
# 두번째 시도 DP
n = int(input())
due = []
cost = []
for _ in range(n):
    d, c = map(int, input().split())
    due.append(d)
    cost.append(c)
dp = [0] * n
for i in range(0, n):
    max_dp = 0
    for j in range(0, i):
        if j + due[j] - 1 < i:
            max_dp = max(max_dp, dp[j])
    if i + due[i] - 1 < n:
        dp[i] = max_dp + cost[i]
print(max(dp))
# 첫번째 시도 그리디 -> 해결할 수 없는 반례가 존재함
n = int(input())
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, input().split())))
result = [False] * n
for i in range(n - 1, -1, -1):
    due, cost = meetings[i]
    if i + due - 1 < n:
        if not any(result[i:i+due]):
            result[i] = True
        else:
            prev = 0
            for j in range(i + 1, i + due):
                if result[j]:
                    prev += meetings[j][1]
            if cost > prev:
                result[i] = True
                for j in range(i + 1, i + due):
                    result[j] = False
    print(result)
print(sum([meetings[i][1] for i in range(n) if result[i]]))