# https://www.acmicpc.net/problem/2309
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
d_sum = sum(dwarfs)
stop = False
for i in range(9):
    if stop: break
    for j in range(i + 1, 9):
        if d_sum - dwarfs[i] - dwarfs[j] == 100:
            dwarfs.pop(j)
            dwarfs.pop(i)
            dwarfs.sort()
            print(*dwarfs, sep="\n")
            stop = True
            break