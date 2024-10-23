#  N(1 ≤ N ≤ 8)이 주어질 때 1~n으로 이뤄진 순열 출력
# 결과에 도달할 때 마다 출력해버리면 되나



def permute(N):
    def backtrack(curr, used):
        if len(curr) == N:
            print(" ".join(map(str,curr)))
            return
        
        for i in range(1, N+1):
            if i not in used:
                curr.append(i)
                used.add(i) #방문 여부 기록
                backtrack(curr,used)
                curr.pop()
                used.remove(i)#방문 여부 삭제
    
    backtrack([],set())

N = int(input())
permute(N)