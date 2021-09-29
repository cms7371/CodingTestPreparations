# https://www.acmicpc.net/problem/7575
import sys
input = sys.stdin.readline


def get_pi(search):
    l = len(search)
    pi = [0] * l
    begin, matched = 1, 0
    while begin + matched < l:
        if search[begin + matched] == search[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


def KMP_find(src, search):
    l, m = len(src), len(search)
    pi = get_pi(search)
    begin, matched = 0, 0
    while begin <= l - m:
        if matched < m and src[begin + matched] == search[matched]:
            matched += 1
            if matched == m:
                return True
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return False


def all_include(candidates, search):
    rev_search = search[::-1]
    for candidate in candidates:
        if not (KMP_find(candidate, search) or KMP_find(candidate, rev_search)):
            return False
    return True


def check_virus(determinant, others, k):
    for idx in range(len(determinant) - k + 1):
        sub = determinant[idx: idx + k]
        if all_include(others, sub):
            print("YES")
            return
    print("NO")
    return


N, K = map(int, input().split())
_ = int(input())
shortest = list(map(int, input().split()))
programs = []
for _ in range(N - 1):
    cur_l = int(input())
    cur_p = list(map(int, input().split()))
    if cur_l < len(shortest):
        programs.append(shortest)
        shortest = cur_p
    else:
        programs.append(cur_p)
check_virus(shortest, programs, K)


