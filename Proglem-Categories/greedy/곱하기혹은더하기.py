#0일 때만 + , 그 외는 x 마지막은 연산자 안함

nums = input()

#초기값 0으로 안잡도록 주의!
result = int(nums[0])

for i in range(1, len(nums)):
    #result(앞), i(뒤) 둘 중 하나라도 0 or 1 -> + 연산
    num = int(nums[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)