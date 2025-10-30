def solution(s):
    answer = True
    n = 0
    for x in s:
        if x == '(':
            n+=1
        else: 
            n-=1
            if n <0:
                break
    if n !=0 :
        answer = False

    return answer