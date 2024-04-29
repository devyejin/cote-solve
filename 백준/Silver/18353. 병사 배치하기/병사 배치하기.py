N = int(input()) #수열 길이
power = list(map(int, input().split()))

d = [1] * N #d[i] : power[i]를 마지막 수로 하는 감소하는 가장 긴 수열의 길이

for i in range(N):
    for j in range(i):
        if power[i] < power[j]:
            d[i] = max(d[i], d[j]+1)

print(N - max(d))