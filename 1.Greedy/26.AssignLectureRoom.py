# 강의실 배정하기 https://www.acmicpc.net/problem/11000
from heapq import *


n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]


