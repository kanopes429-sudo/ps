def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    
    while queue:
        cur = queue.pop(0)
        if any(p[1] > cur[1] for p in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer