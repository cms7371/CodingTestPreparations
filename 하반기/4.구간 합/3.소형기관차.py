# https://www.acmicpc.net/problem/2616
# https://kjwsx23.tistory.com/398 자세한 풀이
# 이해한대로 써보자면 dp를 이용해서(누적합도 사용되지만 주된 컨셉은 dp) 열차의 개수를 늘려가며 테이블을 구함
# 이때 적은 열차부터, dp를 구함. 각 케이스는 현재 탐색하는 열차를 고르는 경우와 고르지 않는 경우로 나누어진다. 이때
# 현재 선택한 열차를 고르지 않는다는 것은 이전 dp값을 그대로 가져오는 것이고, 현재 탐색하는 열차를 고르는 것은
# 이 열차와 엮여있는 열차들을 고르면 안되는 것으로 열차가 하나 더 적은 테이블의 i - m + 1자리의 값을 참조하여 이것에 현재 열차를
# 선택했을 때의 값을 담는 것임
n = int(input())
trains = [0] + list(map(int, input().split()))
m = int(input())
for i in range(1, n + 1):
    trains[i] += trains[i - 1]  # 누적합으로 구하기 쉽게 함
dp = [[0] * (n + 1) for _ in range(4)]  # 인덱스를 i, j라고 했을 때 i는 열차의 대수, j는 j번째 화물까지 보았을때
for i in range(1, 4):  # 열차가 1~3개일 때
    for j in range(m, n + 1):  # j번째 화물까지 보았을 때 dp를 구함
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - m] + trains[j] - trains[j - m])
print(dp[-1][-1])