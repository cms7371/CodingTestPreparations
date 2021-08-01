# https://www.acmicpc.net/problem/14889
from itertools import combinations
n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]
avoid_dup_set = set()
combs = combinations(range(n), n // 2)
result = 10e9
for comb in combs:  # 모든 팀 조합을 탐색함
    team = tuple(comb)
    if team in avoid_dup_set:  # 이때 중복되는 경우를 방지해주기 위해 set을 이용하여 이미 검사한 조합인지 확인
        continue

    avoid_dup_set.add(team)  # 아니라면 두 팀을 모두 set에 넣어주어 중복 방지
    opposite_team = tuple(set(range(n)).difference(team))
    avoid_dup_set.add(team)
    avoid_dup_set.add(opposite_team)

    team_syn = 0  # 각 팀의 synergy를 검사함
    opposite_syn = 0
    for i, j in combinations(team, 2):
        team_syn += synergy[i][j] + synergy[j][i]
    for i, j in combinations(opposite_team, 2):
        opposite_syn += synergy[i][j] + synergy[j][i]
    result = min(result, abs(team_syn - opposite_syn))
print(result)



