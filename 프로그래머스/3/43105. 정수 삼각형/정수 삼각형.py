def solution(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
            answer = triangle[0][0]            
    return answer

def solution2(triangle2):
    dp = [row[:] for row in triangle2]
    
    for i in range(len(triangle2)-2,-1,-1):
        for j in range(len(triangle2[i])):
            dp[i][j] = triangle2[i][j] + max(dp[i+1][j], dp[i+1][j+1])
            
    return dp[0][0]