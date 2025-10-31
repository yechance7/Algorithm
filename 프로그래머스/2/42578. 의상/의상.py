def solution(clothes):
    answer = 1
    closet = {}
    
    for n in clothes:
        x,y = n
        if y not in closet.keys():
            closet[y] = list()
        closet[y].append(x)

    for key, val in closet.items():
        answer = answer* (len(val)+1)
        
    return answer -1