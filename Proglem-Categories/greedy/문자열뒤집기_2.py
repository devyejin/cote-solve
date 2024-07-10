import sys
input = sys.stdin.readline

word = input().rstrip()

cnt_info = {'0':0, '1':0} #'0' : '0'이라 '1'로 바꾸는 횟수

now = word[0]
cnt_info[now] += 1

for num in word:
    if now != num: #이전값과 현재값이 다르다면
        cnt_info[num] += 1
        now = num

print(min(cnt_info.values()))
