# https://www.acmicpc.net/problem/10815
# 두 번째 풀이: 의도한대로 이분 탐색을 이용하기
def bisect_left(arr, val):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > val:
            r = mid - 1
        elif arr[mid] < val:
            l = mid + 1
        else:
            l = r = mid
            break
    if l == r:
        return l
    else:
        return -1 if r == -1 else len(arr)


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))
cards.sort()
for q in queries:
    print(1 if 0 <= bisect_left(cards, q) < n else 0, end=" ")


# 첫 풀이: 매우 간단하게 set을 이용하는 방법
# n = int(input())
# cards = set(map(int, input().split()))
# m = int(input())
# queries = list(map(int, input().split()))
# for q in queries:
#     print(1 if q in cards else 0, end=" ")
