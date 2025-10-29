def solution(answers):
    
    s1 = [1, 2, 3, 4, 5]*2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

    count = [0,0,0]
    for n, x in enumerate(answers):
        for m, y in enumerate([s1,s2,s3]):
            if y[n] == x:
                count[m] +=1
                
    answer=[]
    for n, z in enumerate(count):
        if z == max(count):
            answer.append(n+1)
    
    
    return answer