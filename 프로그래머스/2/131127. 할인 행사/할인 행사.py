def solution(want, number, discount):
    answer = 0
    wanna = dict(zip(want, number))
    # wanna ={}
    # for i in range(len(want)):
    #   wanna[want[i]] = number[i]
    for i in range(len(discount)-9):
        ten_days = discount[i : i+10]   # 그날부터 10일
        
        for item in wanna:
            if ten_days.count(item) < wanna[item]:
                break
        else: answer += 1
            
    return answer