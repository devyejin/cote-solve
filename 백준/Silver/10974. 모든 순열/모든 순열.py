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