def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            answer[i] += 1   # 1초 지났다고 카운트
            
            # 나보다 가격이 떨어지면 반복문 중단
            if prices[j] < prices[i]:
                break
        
    return answer