# 10755번 공항 https://www.acmicpc.net/problem/10775
# 복습 풀이
import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
parents = [i for i in range(g + 1)]
def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]
def union(a, b):
    parents[b] = find(a)
result = 0
for p in planes:
    if find(p) == 0:
        break
    else:
        result += 1
        union(find(p) - 1, find(p))
print(result)




# 세번째 : 서로소 집합을 이용함(참고 https://mygumi.tistory.com/245 아주 멋있는 설명)
def find_parent(a):
    if gates[a] == a:
        return a
    else:
        gates[a] = find_parent(gates[a])
        return gates[a]


def union(a, b):
    gates[a] = find_parent(b)


g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
gates = [i for i in range(g + 1)]
result = 0
for p in planes:
    if find_parent(p) == 0:
        break
    elif find_parent(p) == p:
        union(p, p - 1)
    else:
        parent = find_parent(p)
        union(parent, parent - 1)
    result += 1
    # 다른 방법
    docking = find_parent(p)
    if p != 0:
        union(p, p - 1)
        result += 1
print(result)

# 두번째 : bisect를 이용하여 하나씩 게이트에 넣음 -> 오른쪽 boundary를 찾았을 때 비행기의 값보다 크다? 주차할 수 없다는 것이므로 멈춤
# 실패 -> 4 4 3 3 3 의 경우 4가 하나 밀리게 되어 도킹할 수 없음에도 불구하고 도킹이 되는 것으로
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


# 1번째 : recursive 하게 dp테이블을 탐색하여 남은 자리 찾기 -> 시간 초과로 실패
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
