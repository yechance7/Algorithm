from collections import Counter

def solution(nums):
    count = Counter(nums)
    if len(count) >= len(nums)/2:
        answer = len(nums)/2
    else: 
        answer = len(count)
    return answer