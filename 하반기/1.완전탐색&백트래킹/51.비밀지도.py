# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    table = [[False] * n for _ in range(n)]
    for i in range(n):
        code = arr1[i] | arr2[i]
        binary_code = bin(code)[2:]
        print(i, binary_code)
        for idx in range(-1, -len(binary_code) - 1, -1):
            if binary_code[idx] == '1':
                table[i][idx] = True
    answer = ["".join(map(lambda b: "#" if b else " ", line)) for line in table]
    return answer