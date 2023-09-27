import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_point = 0                                       

for i in range(N - 2):                             
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            point = cards[i] + cards[j] + cards[k]  
            if max_point < point <= M:              
                max_point = point                   

print(max_point)