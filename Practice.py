



test_ans = [0] * 10
for i in range(1, N + 1):
    for c in str(i):
        test_ans[int(c)] += 1
print(*test_ans)