# 10755번 공항 https://www.acmicpc.net/problem/10775
# 두번째 : bisect를 이용하여 하나씩 게이트에 넣음 -> 오른쪽 boundary를 찾았을 때 비행기의 값보다 크다? 주차할 수 없다는 것이므로
# 멈추면 됨
import bisect
g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
airport = []
for i in range(len(planes)):
    position = bisect.bisect_right(airport, planes[i])
    if position >= planes[i]:
        print(i)
        break
    else:
        airport.insert(position, planes[i])




# recursive 하게 dp테이블을 탐색하여 남은 자리 찾기 -> 시간 초과로 실패
def dock(n):
    while n != 0:
        if not dp[n - 1]:
            dp[n - 1] = True
            return True
        else:
            n -= 1
    return False


g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
dp = [False] * g
result = 0
for plane in planes:
    if dock(plane):
        result += 1
    else:
        break
print(result)

