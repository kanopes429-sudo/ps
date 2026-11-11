def solution(clothes):
    count = {}
    for name, kind in clothes:
        if kind in count:
            count[kind] += 1
        else:
            count[kind] = 1
            
    answer = 1
    for n in count.values():
        answer = answer * (n + 1)
        
    return answer - 1