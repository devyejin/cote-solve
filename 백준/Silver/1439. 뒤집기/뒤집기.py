
datas = input()

cnt_change = 0
for i in range(len(datas) -1):
    if datas[i] != datas[i+1]:
        cnt_change += 1

print((cnt_change+1)//2)