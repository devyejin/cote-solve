n, l = map(int,input().split())

hlist = list(map(int, input().split()))
hlist.sort()


for _ in range(n):
    if hlist.pop(0) <= l:
        l += 1
    else:
        break

print(l)