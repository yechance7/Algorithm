def solution(prices):
    answer = []
    for n, price in enumerate(prices):
        count = 0
        for m in range(len(prices)-n-1):
            count +=1
            if price >  prices[m+n+1]:
                break
        answer.append(count)
        
    return answer