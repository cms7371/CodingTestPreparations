# https://www.acmicpc.net/problem/1644
N = int(input())
isPrime = [True] * (N + 1)
for i in range(2, N + 1):
    if isPrime[i]:
        idx = i * 2
        while idx <= N:
            isPrime[idx] = False
            idx += i
primes = []
for i in range(2, N + 1):
    if isPrime[i]:
        primes.append(i)
s, e, cur, result = 0, 0, 0, 0
while s < len(primes):
    if e < len(primes) and cur < N:
        cur += primes[e]
        e += 1
    else:
        cur -= primes[s]
        s += 1
    if cur == N:
        result += 1
print(result)