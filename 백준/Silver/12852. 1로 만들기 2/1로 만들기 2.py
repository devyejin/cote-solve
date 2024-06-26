#dp 테이블
# d = [0] * 1000001 # <- 공간낭비되니까
x = int(input())

d = [0] * (x+1)
d[1] = 0

history = [0] * (x+1)


for i in range(2, x+1):
    d[i] = d[i-1]  + 1
    history[i] = i-1

    if i % 3 == 0 and d[i] > d[i //3] + 1:
        d[i] = d[i//3] + 1
        history[i] = i // 3

    if i % 2 == 0 and d[i] > d[i //2] + 1:
        d[i] = d[i//2] + 1
        history[i] = i // 2


print(d[x])

while x != 0:
    print(x, end=" ")
    x = history[x]