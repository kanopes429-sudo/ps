def solution(progresses, speeds):
    days_list = []
    
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        remain = 100 - progress
        days = remain // speed
        
        if remain % speed != 0:
            days += 1
            
        days_list.append(days)
        
    answer = []
    deploy_day = days_list[0]
    count = 0
    
    for days in days_list:
        if days <= deploy_day:
            count += 1
        else:
            answer.append(count)
            deploy_day = days
            count = 1
            
    answer.append(count)
    return answer