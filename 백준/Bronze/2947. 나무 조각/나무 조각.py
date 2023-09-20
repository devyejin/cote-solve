import sys
input = sys.stdin.readline

woods = list(map(int, input().split()))

while woods != [1, 2, 3, 4, 5]:

    for i in range(1,5):
        if woods[i - 1] > woods[i]:
            woods[i -1] , woods[i] = woods[i], woods[i -1]
            print(*woods) # * : 리스트 요소들을 언패킹해서 출력 즉, [1,2,3,4,5] => 1 2 3 4 5로 출력해줌