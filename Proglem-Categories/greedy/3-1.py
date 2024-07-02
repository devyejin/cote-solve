#거스름돈
n = 1260
count = 0
list = [100, 500, 50, 10] #잔돈

list = sorted(list, reverse=True) #O(nlogn)

for coin in list:
    count += n // coin
    n %= coin 

print(count) #6