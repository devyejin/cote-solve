import sys

input = sys.stdin.readline
meetings = []

n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((end, start))

meetings.sort()

result = 0
current_end_time = 0

#현재 종료 시간 <= 시작 시간 and 종료시간이 가장 짧은 것(정렬로 처리)
for end, start in meetings:
    if current_end_time <= start:
        result += 1
        current_end_time = end

print(result)