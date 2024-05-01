# N : 도감에 수록된 포켓몬 개수
# M : 맞춰야 하는 문제의 개수 ( 1<= N,M <= 100,000)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dict_num_key = {}
dict_name_key = {}

for i in range(1, N+1):
    name = input().strip() #개행 제거
    dict_num_key[i] = name
    dict_name_key[name] = i

for i in range(M):
    item = input().strip() #개행 제거
    if item.isdigit(): # True는 생략해도 됨
        print(dict_num_key[int(item)])
    else:
        print(dict_name_key[item])


