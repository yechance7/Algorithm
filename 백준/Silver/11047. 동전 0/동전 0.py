import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coin_value = int(sys.stdin.readline())
    coins.append(coin_value)

count = 0
for n in range(N-1,-1,-1):
    if K//coins[n] !=0:
        count += K//coins[n]
        K = K%coins[n]
        if K ==0:
            break
    
print(count)