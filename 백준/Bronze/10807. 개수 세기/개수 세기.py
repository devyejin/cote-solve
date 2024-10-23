N = int(input())
arr = input().split()
v = input()
result = 0

for ele in arr:
  if ele == v:
    result += 1

print(result)
