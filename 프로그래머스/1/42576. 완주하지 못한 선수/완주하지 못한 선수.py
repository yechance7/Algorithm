def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for n in range(len(completion)):
        if participant[n] != completion[n]: 
            return participant[n]
    return participant[-1]