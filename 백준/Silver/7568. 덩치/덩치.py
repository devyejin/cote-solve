# 등수 : count ( 본인보다 더 큰 수 ) + 1

n = int(input())
people = []
ranking = [1] * n

#데이터 받고
for _ in range(n):
    weight, height = map(int, input().split())
    person_tuple = (weight, height)
    people.append(person_tuple)

#비교
for now in range(n-1):
    now_w, now_h = people[now]
    for other in range(now + 1, n):
        other_w, other_h = people[other]
        if now_w > other_w and now_h > other_h:
            ranking[other] += 1
        elif now_w < other_w and now_h < other_h:
            ranking[now] += 1

print(*ranking)