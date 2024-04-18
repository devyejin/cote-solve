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
