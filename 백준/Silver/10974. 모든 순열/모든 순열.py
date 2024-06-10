def permute(N):
    def backtrack(curr):
        if len(curr) == N:
            print(" ".join(map(str,curr)))
            return
        
        for i in range(1, N+1):
            if i not in curr:
                curr.append(i)
                backtrack(curr)
                curr.pop()
        
    backtrack([])

N = int(input())
permute(N)