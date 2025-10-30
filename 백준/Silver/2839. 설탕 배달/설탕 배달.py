import sys

N = int(sys.stdin.readline())


for n in range(N//5,-1,-1):
    count = (N-5*n)//3
    if (N-5*n)%3 ==0:
        print(n+count)
        sys.exit(0)
        
print(-1)