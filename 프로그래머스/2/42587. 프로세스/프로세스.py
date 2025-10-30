def solution(priorities, location):
    answer = 0
    max_val = max(priorities)
    n=0
    while priorities[location] != 0:
        if priorities[n] == max_val:
            priorities[n] = 0
            max_val = max(priorities)
            answer +=1
        n+=1 
        if n >= len (priorities):
            n = 0
    return answer