import sys

N1 = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
N2 = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

a = set(A)
answer=[]
for n in B:
    if n in a:
        answer.append('1')
    else:
        answer.append('0')
        
print(' '.join(answer))