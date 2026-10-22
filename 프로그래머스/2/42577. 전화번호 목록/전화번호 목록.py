def solution2(phone_book):
    d = dict(zip(phone_book, [0]*len(phone_book)))
    for num in phone_book:
        for i in range(1,len(num)):
            prefix = num[:i]
            if prefix in d:
                return False
    return True

def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        short = phone_book[i-1]
        long = phone_book[i]
        if long[:len(short)] == short:
            return False
    return True