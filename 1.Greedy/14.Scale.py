# 2437번 저울 https://www.acmicpc.net/problem/2437
# 만약 n까지 무게를 잴 수 있고 새로운 m의 추가 있다면 n + m까지 잴 수 있다는 논리를 재귀적으로 이용하여 해결하는 문제
n = int(input())
weights = list(map(int, input().split()))
weights.sort(reverse=True)
current = 1
while weights:
    w = weights.pop()
    if w <= current:
        current += w
    else:
        break
print(current)

# 힌트 참고함 https://www.acmicpc.net/board/view/45841
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
current = 0
while data:
    c = data.pop()
    if c <= current + 1:
        current += c
    else:
        break
print(current + 1)
