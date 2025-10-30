def solution(arr):
    answer = []
    for n, v in enumerate(arr):
        if n == len(arr) -1:
            answer.append(v)
            break
        if arr[n] != arr[n+1]:
            answer.append(v)
    return answer