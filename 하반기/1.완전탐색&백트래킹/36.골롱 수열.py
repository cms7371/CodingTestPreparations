# https://blog.naver.com/kks227/220795165570
N = int(input())
arr = [0, 1]
p, q = 1, 1
while q < N:
    p += 1
    arr.append(arr[-1] + 1 if arr[-arr[arr[-1]]] == arr[-1] else arr[-1])
    q += arr[-1]
print(p)