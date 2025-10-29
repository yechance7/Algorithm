def solution(n, lost, reserve):
    self_helped = set(lost) & set(reserve)
    lost = set(lost) - self_helped
    reserve = set(reserve) - self_helped
    
    for stu in reserve:
        if stu-1 in lost:
            lost.remove(stu-1)
        elif stu+1 in lost:
            lost.remove(stu+1)
    
    answer = n- len(lost)
    return answer