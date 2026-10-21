def solution(want, number, discount):
    answer = 0
    wanna = dict(zip(want, number))
    # wanna ={}
    # for i in range(len(want)):
    #   wanna[want[i]] = number[i]
    for i in range(len(discount)-10+1):
        ten_days = discount[i : i+10]   # 그날부터 10일
        
        ok = True
        for item in wanna:
            if ten_days.count(item) < wanna[item]:
                ok = False
                
        if ok:
            answer += 1
            
    return answer