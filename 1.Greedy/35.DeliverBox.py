# 8980번 택배 https://www.acmicpc.net/problem/8980
# 풀이 참고 https://www.acmicpc.net/board/view/6327
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
