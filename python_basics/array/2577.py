# fruits = ['apple', 'banana', 'cherry','banana','banana']

# #banana가 몇 개 들어 있는가
# count = fruits.count('banana')
# print(count)

result = 1
for _ in range(3):
  result *= int(input())

result = str(result)
answer = [0 for _ in range(10)]
for char in result:
  answer[int(char)] = result.count(char)

for ans in answer:  
  print(ans)