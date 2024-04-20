# msg = "{}번 원반을 {} -> {} 이동"

# def move(N, start, to):
#     print(msg.format(N, start, to))

# def hanoi(N, start, to, via):
#     if N == 1:
#         move(1, start, to)
#     else:
#         hanoi(N-1, start, via, to)
#         move(N, start, to)
#         hanoi(N-1, via, to, start)


# hanoi(3,1,3,2)


N = int(input())


def move(N, start, to):
    print(f"{start} {to}")

    
def hanoi(N, start, to, via):
    if N == 1:
        move(N, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)
    
print(2 ** N - 1)    
hanoi(N,1,3,2)
