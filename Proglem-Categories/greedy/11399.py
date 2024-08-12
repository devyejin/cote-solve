import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()

times = []
current_time = 0

for time in p:
    current_time += time
    times.append(current_time)

print(times)
print(sum(times))