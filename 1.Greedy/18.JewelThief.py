# 1202번 보석 도둑 https://www.acmicpc.net/problem/1202
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
