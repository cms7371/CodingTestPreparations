# https://www.acmicpc.net/problem/2798
n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)  # 큰 수부터 탐색하는 것으로 함
result = 0
for i in range(n - 2):
    if cards[i] >= m:  # 가장 큰 카드가 m 보다 크면 스킵
        continue
    for j in range(i + 1, n - 1):
        if cards[i] + cards[j] >= m:  # 두번째 카드까지 합이 m보다 커도 스킵
            continue
        for k in range(j + 1, n):
            temp = cards[i] + cards[j] + cards[k]  # 세번째 카드까지의 합이
            if temp > m:  # m보다 크면 더 작은 3번째 카드를 찾아야 되므로 스킵
                continue
            elif temp > result:  # 지금까지 구한 값보다 크다면 저장 후 다음 두번째 카드로
                result = temp
                break
            else:  # 구한 값보다 작다면 앞으로 값은 더 작을 것이므로 다음 두번째 카드로 넘어감
                break
print(result)