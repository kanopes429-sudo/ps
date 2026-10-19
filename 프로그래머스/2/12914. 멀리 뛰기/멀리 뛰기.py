def factorial(k):
    result = 1
    for i in range(1, k+1):
        result = result * i
    return result

def solution(n):
    answer = 0
    for y in range(0, n // 2 + 1):
        x = n - 2 * y
        ways = factorial(x + y) // (factorial(x) * factorial(y))
        answer += ways
    return answer % 1234567