word = input()
char_cnt = [0 for _ in range(26)]

for char in word:
  num = ord(char) - ord('a')
  char_cnt[num] += 1

print(*char_cnt)