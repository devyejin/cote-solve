# 마지막 요소 -2 고려하면 좋은 코드는 아닌거같음
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# numbers = list(map(int,input().split()))
# numbers.sort()
#
# print(numbers.pop(0),numbers.pop(N-2))

# 반례를 생각한다면, element가 2개밖에 없는 경우 최소,최대는 있는데 이 로직은 못써먹음

import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))