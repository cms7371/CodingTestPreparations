# 1041번 주사위 https://www.acmicpc.net/problem/1041
comb2 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
comb3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
n = int(input())
dice = list(map(int, input().split()))
if n == 1:
    dice.sort()
    dice.pop()
    print(sum(dice))
else:
    case1 = min(dice)
    case2 = min([dice[case[0]] + dice[case[1]] for case in comb2])
    case3 = min([dice[case[0]] + dice[case[1]] + dice[case[2]] for case in comb3])
    print(case1 * (5 * n * n - 16 * n + 12) + case2 * (8 * n - 12) + case3 * 4)
