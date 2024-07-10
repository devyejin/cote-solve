import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()

times = [0] * n
current_time = 0

for i in range(n):
    current_time += p[i]
    times[i] = current_time
    
print(sum(times))