from collections import Counter

def solution(k, tangerine):
    answer = 0
    counts = sorted(Counter(tangerine).values(), reverse=True)
    total = 0
    for cnt in counts:
        total += cnt
        answer += 1
        if total >= k:
            return answer
    return answer