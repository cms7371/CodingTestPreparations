from itertools import combinations
L, C = map(int, input().split())
vowel = ["a", "e", "i", "o", "u"]
arr = input().split()
arr.sort()
candidates = combinations(arr, L)
for cur in candidates:
    count = 0
    for c in cur:
        if c in vowel:
            count += 1
    if 0 < count < L - 1:
        print("".join(cur))