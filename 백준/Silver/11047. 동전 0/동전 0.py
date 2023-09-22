
N, K = map(int,input().split())
unit = []
count = 0

for _ in range(N):
    unit.append(int(input()))

unit = unit[::-1]

for coin in unit:
    count += K // coin
    K %= coin

print(count)