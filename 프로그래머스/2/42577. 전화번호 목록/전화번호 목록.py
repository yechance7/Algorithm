from collections import Counter
def solution(phone_book):
    answer = True
    count = Counter(phone_book)
    for n in phone_book:
        length = len(n)-1
        while length != 0 and len(n) != 0:
            if n[0:length] in count:
                answer = False
            length-=1
    return answer