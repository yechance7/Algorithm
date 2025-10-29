from collections import Counter

def solution(participant, completion):
    participant_counts = Counter(participant)
    for name in completion:
        participant_counts[name]-=1
        
    for name, count in participant_counts.items():
        if count > 0:
            return name