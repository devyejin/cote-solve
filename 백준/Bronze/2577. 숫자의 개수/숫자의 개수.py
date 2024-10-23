result = 1
for _ in range(3):
  result *= int(input())

result = str(result)
answer = [0 for _ in range(10)]
for char in result:
  answer[int(char)] = result.count(char)

for ans in answer:  
  print(ans)