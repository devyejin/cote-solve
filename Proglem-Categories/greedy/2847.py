import sys

input = sys.stdin.readline

n = int(input())
scores = []

for _ in range(n):
    scores.append(int(input()))

result = 0

for i in range(n):
    result += - (scores[i] - scores[n-1] - (n-1-i))

print(result)