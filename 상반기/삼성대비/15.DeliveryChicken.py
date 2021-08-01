# 15686번 치킨 배달 https://www.acmicpc.net/problem/15686
from itertools import combinations


def get_chicken_distance(row, col, case):
    min_dist = 10e9
    for c_row, c_col in case:
        current_dist = abs(row - c_row) + abs(col - c_col)
        min_dist = min(min_dist, current_dist)
    return min_dist


n, m = map(int, input().split())
town_map = [list(map(int, input().split())) for _ in range(n)]
chicken_sellers = []
houses = []
for i in range(n):
    for j in range(n):
        if town_map[i][j] == 1:
            houses.append((i, j))
        elif town_map[i][j] == 2:
            chicken_sellers.append((i, j))
chicken_cases = combinations(chicken_sellers, m)
result = 10e9
for current_case in chicken_cases:
    current_result = 0
    for h in houses:
        current_result += get_chicken_distance(*h, current_case)
    result = min(result, current_result)
print(result)




