def solution(arr):
    answer = []
    for n,m in enumerate(arr):
        if n==0 :
            answer.append(m)
        elif m != answer[-1]:
            answer.append(m)
    return answer