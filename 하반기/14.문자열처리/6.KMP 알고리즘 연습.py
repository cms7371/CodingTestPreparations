# https://injae-kim.github.io/dev/2020/07/23/all-about-kmp-algorithm.html


def KMP_match(src, search):
    pi = get_partial_match(search)
    l = len(src)
    m = len(search)
    begin = 0
    matched = 0
    result = []
    while begin <= l - m:
        if matched < m and src[begin + matched] == search[matched]:
            matched += 1
            if matched == m:
                result.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return result


def get_partial_match(search):
    """
    KMP 알고리즘을 위한 pi 배열 반환하는 것
    i 자리까지의 substring 을 보았을 때 prefix, suffix 가 몇개가 일치하는지
    """
    l = len(search)
    pi = [0] * l
    begin = 1
    matched = 0
    while begin + matched < l:
        if search[matched] == search[begin + matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


print(KMP_match([0, 1, 2, 3, 4], [2, 3, 4]))
