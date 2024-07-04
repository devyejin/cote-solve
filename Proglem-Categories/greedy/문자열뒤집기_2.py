import sys
input = sys.stdin.readline

word = input().rstrip()

cnt_info = {'0':0, '1':0}

now = word[0]
cnt_info[now] += 1

for num in word:
    if num != now:
        cnt_info[num] += 1
        now = num

print(min(cnt_info.vales()))