# 1202번 보석 도둑 https://www.acmicpc.net/problem/1202
# 작은 가방부터 시작해서 보석을 가벼운 것부터 들어가는대로 PQ에 넣고 더이상 넣을 것이 없으면 가장 비싼걸 pop
# 그 후 다음 가방으로 넘어감(PQ는 그대로). 그 후 또 제일 비싼거 pop
import heapq


n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort(key=lambda x: x[0], reverse=True)
bags.sort()
result = 0
q = []
for b in bags:
    while jewels and jewels[-1][0] <= b:
        j = jewels.pop()
        heapq.heappush(q, -j[1])
    if q:
        result -= heapq.heappop(q)
print(result)


# 정렬을 잘 해서 최적의 해를 구하는 방법 -> 시간 복잡도가 O(nk)로 시간 초과 실패
n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort(reverse=True, key=lambda x: x[0])  # 무게로 내림차순 정렬
jewels.sort(reverse=True, key=lambda x: x[1])  # 가치로 내림차순 정렬
bags.sort()  # 내림차순으로 정렬(뒤에서부터 호출)
result = 0
while bags:
    current = bags.pop()
    for i in range(len(jewels)):
        if jewels[i][0] <= current:
            result += jewels[i][1]
            del jewels[i]
            break
print(result)
