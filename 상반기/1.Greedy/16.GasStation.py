# 13305번 주유소 https://www.acmicpc.net/problem/13305
# 복습 풀이
n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0
current = 0
while current != n - 1:
    destination = current + 1
    while destination < n - 1:
        if cost[destination] < cost[current]:
            break
        else:
            destination += 1
    result += cost[current] * sum(distance[current:destination])
    current = destination
print(result)


# 첫 풀이
n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))
position = 0
result = 0
while position != n - 1:
    stop_position = position + 1
    current_cost = costs[position]
    while costs[stop_position] > current_cost:
        if stop_position == n - 1:
            break
        stop_position += 1
    result += sum(distances[position:stop_position]) * current_cost
    position = stop_position
print(result)


