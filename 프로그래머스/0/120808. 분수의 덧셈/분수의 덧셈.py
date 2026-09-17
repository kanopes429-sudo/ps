def solution(numer1, denom1, numer2, denom2):
    answer = []
    n = (numer1 * denom2) + (numer2 * denom1)
    d = denom1 * denom2
    a, b = n, d
    while b != 0:
        a, b = b, a % b
    answer = (n/a, d/a)
    return answer