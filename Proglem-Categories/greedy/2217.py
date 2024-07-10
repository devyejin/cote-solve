import sys

input = sys.stdin.readline

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort() #O(nlogn)

max_weight = 0

for i in range(n): # O(n)
    current_weight = ropes[i] * (n - i)
    if current_weight > max_weight:
        max_weight = current_weight

print(max_weight)