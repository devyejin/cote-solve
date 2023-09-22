rest_money = 1000 - int(input())

unit = [500, 100, 50, 10, 5, 1]
count = 0

for coin in unit:
    count += rest_money // coin
    rest_money %= coin

print(count)