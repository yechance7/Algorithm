def solution(sizes):
    w = 0
    h = 0
    m = 0
    for x,y in sizes:
        if y > x :
            m = x
            x = y
            y = m
        if x > w:
            w = x
        if y > h:
            h = y
        
    answer = w*h
    return answer