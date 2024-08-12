from itertools import cycle

#리스트를 cycle로 무한 반복
my_list = [1,2,3]
cycle_my_list = cycle(my_list)

# my_list를 10번 반복하고 싶다면
for _ in range(10):
    print(next(cycle_my_list))