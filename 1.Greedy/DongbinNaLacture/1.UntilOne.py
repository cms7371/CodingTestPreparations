# 문제
# 두 정수 N, K 가 주어졌을 때 N이 K로 나누어지는 경우 나누고 그렇지 않은 경우 N에서 1을 뺐을 때
# N이 1이 될 때까지 반복해야하는 최소 횟수를 구하여라

# 내 코드
n, k = map(int, input().split())

counter = 0

while n != 1:
    n = n // k if (n % k) == 0 else n - 1
    counter += 1
print(counter)

# 제시된 코드
n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)
print(result)
# 반복문을 줄여서 O(log)로 복잡도를 줄일 수 있음
