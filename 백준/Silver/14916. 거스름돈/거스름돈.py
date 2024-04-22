n = int(input())
result = -1

for i in range(n//5, -1, -1): # 5로 나눴을 때 최대치 몫 ~ 0 까지, 1씩 줄이며
   # n - (5 * 몫) = 나머지
    if( (n - (5*i)) % 2 == 0  and (n - (5*i)) >= 0):
        result = i + (n - (5*i))//2 # 5로 나눈 몫 + 나머지를 2로 나눈 몫
        break

print(result) #만일 해가 없다면 result = -1 반환되겠지