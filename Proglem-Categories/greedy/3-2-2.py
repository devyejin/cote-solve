# 5 8 3
# 2 4 5 4 6

# 배열의 크기 N, 숫자 더해지는 횟수 M, 연속해서 K번까지 더할 수 있음
# 가장 큰 수를 만들어라! => 가장 큰 수 K번 더하고 + 두번쨰로 큰 수 1번 + 가장 큰 수 K번 ...
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #정렬
first = data[N-1]
second = data[N-2]

result = 0

#가장 큰 수가 더해지는 횟 수
count = (M // (K+1)) * K
count += M % (K+1)

#두번째로 큰 수는 M -count 번
result += (count) * first
result += (M-count) * second

print(result)