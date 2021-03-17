# 8980번 택배 https://www.acmicpc.net/problem/8980
# 풀이 참고 https://www.acmicpc.net/board/view/6327
n, c = map(int, input().split())
m = int(input())
box = [list(map(int, input().split())) for _ in range(m)]
box.sort(key=lambda x: (x[1], x[0]))
dp = [c] * (n + 1)
result = 0
for b in box:
    start, end = b[0], b[1]
    min_cap = min(dp[start:end])
    togo = min(min_cap, b[2])
    result += togo
    dp[start:end] = [i - togo for i in dp[start:end]]
print(result)

# dp 테이블과 그리디를 혼합한 방식으로 푸는 방법. 각 도시마다 여유 용량 테이블을 만들고, 가까운 도착지 순, 가까운 출발지 순으로 정렬함
# 그 후 정렬된 데이터를 앞부터 탐색하며 여유 용량 테이블에 해당되는 마을의 여유용량을 감소시켜줌
n, max_cap = map(int, input().split())
m = int(input())
box_info = []
# 간단한 정렬을 위해서 도착지, 출발지, 갯수 순서로 넣어줌
for _ in range(m):
    start, end, cap = map(int, input().split())
    box_info.append((end, start, cap))
dp = [max_cap] * (n + 1)
box_info.sort()
result = 0
for box in box_info:
    end, start, cap = box
    min_cap = min(dp[start:end])
    if min_cap != 0:
        can_deliver = cap if min_cap >= cap else min_cap
        result += can_deliver
        for i in range(start, end):
            dp[i] -= can_deliver
print(result)
