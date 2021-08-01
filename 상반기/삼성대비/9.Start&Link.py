# 14889번 스타트와 링크 https://www.acmicpc.net/problem/14889
from itertools import combinations
n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]
team_combinations = combinations(range(n), n // 2)
result = 10e9
for comb in team_combinations:
    opposite = list(set(range(n)).difference(comb))
    team = list(comb)

    diff = 0
    for i in range(n//2):
        for j in range(i + 1, n//2):
            diff += synergy[team[i]][team[j]] + synergy[team[j]][team[i]]
            diff -= synergy[opposite[i]][opposite[j]] + synergy[opposite[j]][opposite[i]]
    result = min(result, abs(diff))
print(result)



