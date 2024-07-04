n = int(input())
fears = sorted(list(map(int, (input().split())))) #O(nlogn)

result = 0
count = 0 #팀 인원

for fear in fears:
    count += 1 #인원 한명은 무조건 체크되니까
    if count >= fear:
        result += 1 #팀 결성 끝
        count = 0 #팀 인원 초기화

print(result)