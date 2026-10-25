def solution(clothes):
    answer = 0
    category=[]
    count =[]
    for n in clothes:
        if n[1] not in category:
            category.append(n[1])
            count.append(1)
        else :
            count[category.index(n[1])] +=1
    answer+=1
    for m in count:
        answer*=(m+1)
    return answer -1