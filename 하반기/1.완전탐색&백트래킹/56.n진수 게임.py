# https://programmers.co.kr/learn/courses/30/lessons/17687


def solution(n, t, m, p):
    seq = ''
    i = 0
    while len(seq) < t * m:
        cur_num = i
        num_as_string = ''
        while True:
            digit = cur_num % n
            num_as_string += num_to_c(digit)
            cur_num //= n
            if cur_num == 0:
                break
        seq += num_as_string[::-1]
        i += 1
    answer = "".join(seq[turn - 1] for turn in range(p, t * m + 1, m))
    return answer


def num_to_c(num):
    return str(num) if num < 10 else chr(55 + num)