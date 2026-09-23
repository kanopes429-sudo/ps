def solution(array):
    answer = 0
    max_count = 0
    tie = False
    
    for i in set(array):
        cnt = array.count(i)
        if cnt > max_count:
            answer = i
            max_count = cnt
            tie = False
        elif cnt == max_count:
            tie = True
            
    if tie:
        return -1
    
    return answer

def solution(array):
    # 딕셔너리에 {원소 : 원소 갯수} count 함수 사용해 저장
    dic = {}
    for num in array:
        dic[num] = array.count(num)
    # 가장 많이 나온 반복 수 찾기
    max_val = max(dic.values())
    
    max_keys = []
    for k, v in dic.items():
        if v == max_val:
            max_keys.append(k)
    
    if len(max_keys) >= 2:
        return -1
    else:
        return max_keys[0]