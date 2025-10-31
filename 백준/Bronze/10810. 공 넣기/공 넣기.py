import sys

N, M = map(int, sys.stdin.readline().split())

data = []
for _ in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    data.append(row)
    
answer =[0]*N
for val in data:
    for m in range(val[0]-1,val[1]):
        answer[m] = val[2]

print(' '.join(map(str, answer)))