def solution(bridge_length, weight, truck_weights):
    answer = 0
    bt = [0] * bridge_length
    w = 0
    
    while truck_weights:
        answer += 1
        w -= bt.pop(0)
        if w + truck_weights[0] <= weight:
            t = truck_weights.pop(0)
            w += t
            bt.append(t)
        else:
            bt.append(0)
            
    return answer + bridge_length