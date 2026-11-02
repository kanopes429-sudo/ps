from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    for d in range(2, int(x ** 0.5)+1):
        if x % d == 0:
            return False
    return True

def solution(numbers):
    candidates = set()
    
    for length in range(1, len(numbers)+1):
        for p in permutations(numbers, length):
            num = int("".join(p))
            candidates.add(num)
    
    count = 0
    for num in candidates:
        if is_prime(num):
            count += 1
            
    return count