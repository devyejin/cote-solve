import sys

input = sys.stdin.readline

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort() #O(nlogn)

weights = []

for rope in ropes:
    weights.append(rope * n)
    n -= 1

print(max(weights))