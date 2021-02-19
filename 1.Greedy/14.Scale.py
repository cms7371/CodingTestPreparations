# 2437번 저울 https://www.acmicpc.net/problem/2437
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
