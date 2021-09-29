# https://programmers.co.kr/learn/courses/30/lessons/60060
import sys
from collections import defaultdict
sys.setrecursionlimit(100000)


def init_trie(trie, words):
    trie['?'] = defaultdict(int)
    for s in words:
        cur = trie
        l = len(s)
        trie['?'][l] += 1
        for c in s:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
                cur['?'] = defaultdict(int)
            cur['?'][l] += 1
    return trie


def get_trie(trie, word, l):
    if word == "" or word[0] == '?':
        return trie['?'][l]
    elif word[0] in trie:
        return get_trie(trie[word[0]], word[1:], l)
    else:
        return 0


def solution(words, queries):
    trie = init_trie({}, words)
    rev_words = [s[::-1] for s in words]
    print(rev_words)
    rev_trie = init_trie({}, rev_words)
    answer = []
    for q in queries:
        if q[0] == '?' and q[-1] == '?':
            answer.append(trie['?'][len(q)])
        elif q[-1] == '?':
            answer.append(get_trie(trie, q, len(q)))
        else:
            answer.append(get_trie(rev_trie, q[::-1], len(q)))
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))