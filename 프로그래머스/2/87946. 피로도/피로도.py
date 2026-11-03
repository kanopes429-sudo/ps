from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for route in permutations(dungeons):
        fatigue = k
        num = 0
        for mf, cf in route:
            if mf <= fatigue:
                fatigue -= cf
                num += 1
        answer = max(answer, num)
            
    return answer