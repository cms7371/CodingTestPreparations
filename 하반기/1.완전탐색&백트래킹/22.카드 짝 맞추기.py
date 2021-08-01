# https://programmers.co.kr/learn/courses/30/lessons/72415
# 2021 KAKAO BLIND RECUITMENT


def solution(board, r, c):

    # 1.현재 위치에 대해 모든 거리값 갱신, 이때 카드를 발견하면 힙에 넣어서 가장 가까운 카드를 찾을 수 있도록 함
    y, x = r, c
    
    answer = 0
    return answer