def solution(num, total):
    answer = []
    s = total - (num-1)*num/2
    
    if s % num == 0:
        x = int(s//num)
        answer = list(range(x, x+num))
        
    return answer

def solution(num, total):
    answer = []
    
    num_sum = sum(range(num))
    
    x = int((total - num_sum) / num)
    answer = list(range(x,x+num))
    
    return answer