data = input()
count0 = 0 #0으로 바꾸는 경우
count1 = 0 #1로 바꾸는 경우

#idx=0은 prev값이 없으니까 초기값은 직접 체크
if data[0] == '0':
    count1 += 1
else:
    count0 += 1

#나머지부분 check, prev랑 값이 다르면 변경되는 지점
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))