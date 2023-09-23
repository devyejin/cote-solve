i = 1
while True:
    result = 0
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break

    if 1 < l < p < v:
        result = l * (v // p)

        # if l <= (v % p):
        #     result += l
        # else:
        #     result += (v % p)
        result += min(l, (v % p))

        print(f"Case {i}: {result}")
        i += 1