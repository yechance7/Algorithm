def solution(citations):
    answer = 0
    citations = sorted(citations,reverse=True)
    for n , val in enumerate(citations):
        if n+1 > val :
            answer = n
            return answer
    
    answer = len(citations)    
    
    return answer