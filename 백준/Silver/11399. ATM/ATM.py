n = int(input())
time = sorted(map(int, input().split()))
result = []
accum = 0

for i in time:
    accum += i
    result.append(accum)

print(sum(result))