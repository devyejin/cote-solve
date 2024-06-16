N = int(input())

def solution(N):
    arr_rows = [0] * N # 0 False, 1 Truen로 평가
    arr_cols = [0] * N
    diag_r = [0] * (2 * N - 1)
    diag_l = [0] * (2 * N - 1)
    answer = 0
    
    def deploy_queens(current_depth):
        nonlocal answer
        if current_depth == N:
            answer += 1
            return
        
        for i in range(N):
            if not arr_cols[i] and not diag_r[current_depth - i + N - 1] and not diag_l[current_depth + i ]: #이러면 해당 위치에 놓을 수 있지
                arr_rows[current_depth] = i
                arr_cols[i] = diag_r[current_depth - i + N - 1] = diag_l[current_depth + i] = 1
                deploy_queens(current_depth + 1)
                arr_cols[i] = diag_r[current_depth - i + N - 1] = diag_l[current_depth + i] = 0
    
    deploy_queens(0)
    return answer

result = solution(N)
print(result)