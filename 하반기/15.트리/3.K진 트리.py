# https://www.acmicpc.net/problem/11812
import sys
input = sys.stdin.readline


N, K, Q = map(int, input().split())
for _ in range(Q):
    a, b = map(int, input().split())
    if K == 1:
        print(abs(a - b))
    else:
        answer = 0
        while a != b:
            if a > b:
                a = (a + (K - 2)) // K
            else:
                b = (b + (K - 2)) // K
            answer += 1
        print(answer)