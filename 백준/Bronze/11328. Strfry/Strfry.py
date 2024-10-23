#Counter 이용한 방법
from collections import Counter

N = int(input())
for _ in range(N):
  first, second = input().split()

  if Counter(first) == Counter(second):
    print('Possible')
  else:
    print('Impossible')