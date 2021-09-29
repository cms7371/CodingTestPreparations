# https://programmers.co.kr/learn/courses/30/lessons/42893
import re


def solution(word, pages):
    answer = 0
    word = word.lower()
    N = len(pages)
    page_url = [""] * N
    page_links = [[] for _ in range(N)]
    default_score = [0] * N
    for i, page in enumerate(pages):
        cur_url = re.findall('<meta.+content="(.*)"', page)[0]
        outer_link = re.findall('<a href="([^"]*)"', page)
        page_links[i] = outer_link
        page_url[i] = cur_url
        page_words = re.findall("[a-zA-Z]+", page)
        for w in page_words:
            if w.lower() == word:
                default_score[i] += 1
    print(default_score)
    link_score = [0] * N
    url_to_idx = {url: idx for idx, url in enumerate(page_url)}
    for idx, cur_links in enumerate(page_links):
        if len(cur_links) == 0 or default_score[idx] == 0:
            continue
        for link in cur_links:
            if link in url_to_idx:
                referred_idx = url_to_idx[link]
                link_score[referred_idx] += default_score[idx] / len(cur_links)
    result_score = [default_score[i] + link_score[i] for i in range(N)]
    print(result_score)
    return result_score.index(max(result_score))
