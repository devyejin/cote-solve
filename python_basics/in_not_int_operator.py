#특정 원소가 컨테이너 안에 있는지 판별 => T/F 반환

numbers = [1, 2, 3, 4, 5]

print(1 in numbers) #True
print(7 in numbers) #False
print('a' in numbers) #False


word = "python"

print('w' not in word) #True
print('py' not in word) #False <- 오호, 2글자 이상으로 해도 되네
print('py' in word) #True 

#조건문에서 이용
classroom = ["kyle", "alex", "justin", "jayden"]

if "alex" in classroom:
    print("alex 출석")
else:
    print("alex 결석")