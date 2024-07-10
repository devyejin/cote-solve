import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

result = 0

for i in range(n):
    find_b = max(b)
    b.remove(find_b)
    result += a[i] * find_b

print(result)
    