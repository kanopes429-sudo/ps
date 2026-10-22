def solution(phone_book):
    d = dict(zip(phone_book, [0]*len(phone_book)))
    for num in phone_book:
        for i in range(1,len(num)):
            prefix = num[:i]
            if prefix in d:
                return False
    return True