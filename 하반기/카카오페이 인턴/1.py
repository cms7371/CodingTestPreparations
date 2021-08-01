def solution(money, minratio, maxratio, ranksize, threshold, months):
    balance = money
    t = 0
    while t < months:
        subtract_money = balance - balance % 100
        if subtract_money >= threshold:
            current_ratio = min(minratio + (subtract_money - threshold) // ranksize, maxratio)
            balance -= subtract_money * current_ratio // 100
        t += 1
    return balance


print(solution(12345678, 10, 20, 250000, 10000000, 4))