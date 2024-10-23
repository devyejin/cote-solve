N = int(input())
for _ in range(N):
  result = 'Possible'
  first, second = input().split()

  first_tbl, second_tbl = [0 for _ in range(26)], [0 for _ in range(26)]

  for ch in first:
    first_tbl[ord(ch)-ord('a')] += 1

  for ch in second:
    second_tbl[ord(ch)-ord('a')] += 1

  for i in range(len(first_tbl)):
    #값이 다르다면 Impossible 반환
    if first_tbl[i] != second_tbl[i]:
      result = 'Impossible'
  
  print(result)
