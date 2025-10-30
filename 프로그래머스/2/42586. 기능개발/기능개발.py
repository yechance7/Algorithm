import math
def solution(progresses, speeds):
    answer = []
    max = int(math.ceil((100 - progresses[0])/speeds[0]))
    count = 0
    for n, pro in enumerate(progresses):
        day_cost= int(math.ceil((100 - pro)/speeds[n]))
        if max < day_cost:
            answer.append(count)
            count=0
            max = day_cost
        count +=1
    if count !=0:
        answer.append(count)
    return answer
'''
7 3 9

5 2 7 1 9

'''