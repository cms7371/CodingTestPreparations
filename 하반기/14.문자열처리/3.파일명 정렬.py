# https://programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution(files):
    files.sort(key=get_sep_name)
    return files


def get_sep_name(file):
    head_match = re.match("[^\\d]+", file)
    num_match = re.search("[0-9]+", file)
    head, num = head_match.group(), num_match.group()
    tail = file[num_match.end():]
    return head.lower(), int(num)