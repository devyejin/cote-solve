data = input()
count0 = 0 #0으로 바꾸는 경우
count1 = 1 #1로 바꾸는 경우

if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
#두 번째 원소부터 모든 원소를 확인
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '1': #즉, 이전 수가 0인 경우
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))