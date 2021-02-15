# 피보나치 수열은 재귀적인 방법을 이용하면 2^n의 time complexity를 가지기 때문에 Memoization을 이용하는 것이 도움이 됨
# 이때 큰 수부터 내려가는 탑다운(하향식)과 작은 수부터 계산해서 올라가는 바텀업(상향식)이 있음
# 1. 하향식
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100


def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산된 적이 있다면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


# 바텀업 방식
dp = [0] * 100
dp[1] = 1
dp[2] = 1
n = 99

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])

