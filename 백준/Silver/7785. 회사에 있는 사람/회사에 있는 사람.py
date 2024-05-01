import sys
input = sys.stdin.readline

N = int(input())
company = {}
for _ in range(N):
    man, state = input().rstrip().split()
    if state == 'enter':
        company[man] = True
    else:
        del company[man]

print("\n".join(sorted(company.keys(), reverse=True)))



# set 자료구조 풀이법
n = int(input())
company = set() #entry일 때 저장

for _ in range(n):
    name, status = input().rstrip().split()

    if status == "enter":
        company.add(name)
    elif status == "leave":
        company.remove(name)

#사전 역순으로 정렬해줘야 함, set -> list로 변환해주기
ans = list(company)
ans.sort(reverse=True) #원본 자체를 정렬

for i in range(len(ans)):
    print(ans[i])
