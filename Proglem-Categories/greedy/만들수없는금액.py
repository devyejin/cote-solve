import sys
input = sys.stdin.readline

n = int(input().strip())
coins = list(map(int, list(input().strip())))
coins.sort()

target = 1

for coin in coins:
    # 만들 수 없는 금액을 찾으면 종료
    if target < coin:
        break
    target += coin
    
print(target)
