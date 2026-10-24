def solution(nums):
    answer = 0
    n = []
    for m in nums:
        if m not in n:
            n.append(m)
            answer+=1
    if answer >= (len(nums))/2:
        answer = (len(nums))/2
    return answer