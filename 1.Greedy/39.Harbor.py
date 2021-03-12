# 1092번 배 https://www.acmicpc.net/problem/1092
from bisect import bisect_left, bisect_right
# 두번째 : 그렇다면 pop 대신 disjoint set 을 이용하여 pop을 대신해보자 -> 첫번째 성공해서 안할랭

def find(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]


def union(a, b):
    parents[b] = find(a)


n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort()
parents = [i for i in range(m + 1)]

if crane[0] < box[-1]:
    print(-1)
else:
    iteration = 0
    positions = []
    for c in crane:
        positions.append(bisect_right(box, c))
    while find(m) != 0 and iteration < 10:
        iteration += 1
        for position in positions:
            if not box:
                break
            parent = find(position)
            if parent == 0:
                break
            else:
                union(parent - 1, parent)
    print(iteration)
# 첫번째 : 크래인에서 가능한 모든 박스를 pop 하는 방식으로 구현 -> 시간 초과, 아마도 pop 연산 때문에
# bisect_right로 설계한 것을 left를 써버림... 멍충
n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort()

if crane[0] < box[-1]:
    print(-1)
else:
    iteration = 0
    while box:
        iteration += 1
        for c in crane:
            if not box:
                break
            position = bisect_right(box, c)
            if position == len(box):
                box.pop()
            elif position == 0:
                break
            else:
                box.pop(position - 1)
    print(iteration)
    
    


