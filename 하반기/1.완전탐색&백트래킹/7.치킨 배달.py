# https://www.acmicpc.net/problem/15686
from itertools import combinations
n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]
houses, chickens = [], []
for y in range(n):
    for x in range(n):
        if city_map[y][x] == 1:
            houses.append((y, x))
        elif city_map[y][x] == 2:
            chickens.append((y, x))
cases = combinations(chickens, m)
result = 10e9
for remaining_chickens in cases:
    cnt_result = 0
    for h_y, h_x in houses:
        cnt_dist = 10e9
        for c_y, c_x in remaining_chickens:
            cnt_dist = min(cnt_dist, abs(h_y - c_y) + abs(h_x - c_x))
        cnt_result += cnt_dist
    result = min(result, cnt_result)
print(result)


