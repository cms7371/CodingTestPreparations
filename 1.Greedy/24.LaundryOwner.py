# 세탁소 사장 동혁 https://www.acmicpc.net/problem/2720
n = int(input())
test_cases = [int(input()) for _ in range(n)]
coins = [25, 10, 5, 1]
for case in test_cases:
    for coin in coins:
        print(case // coin, end=" ")
        case %= coin
    print()
