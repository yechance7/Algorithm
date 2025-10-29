def solution(array, commands):
    answer = []
    for x in commands:
        i = x[0] #2
        j = x[1] # 5
        k = x[2] #3
        sliced_array = sorted(array[i-1:j])
        answer.append(sliced_array[k-1])
    return answer