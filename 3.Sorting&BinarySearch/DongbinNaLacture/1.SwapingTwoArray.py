n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort()
a_new = []
for i in range(k):
    a_ = a.pop()
    b_ = b.pop()
    if a_ < b_:
        a_new.append(b_)
    else:
        a.append(a_)
        break
print(sum(a) + sum(a_new))
