
alpha = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
answer = 0
for char in alpha:
  dic[char] = 0

for char in input():
  dic[char] += 1

for char in input():
  dic[char] -= 1

for key in dic:
  answer += abs(dic[key])

print(answer)
