def solution(s):
    answer = ''
    words = s.split(' ')
    result = []
    for word in words:
        new_word = word[:1].upper() + word[1:].lower()
        result.append(new_word)
    answer = ' '.join(result)
    return answer