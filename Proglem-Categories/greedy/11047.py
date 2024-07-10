import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
    
coins = coins[::-1]
print(coins)


result = 0

for coin in coins:
    if k >= coin:
        result += k // coin
        k %= coin
        

print(result)