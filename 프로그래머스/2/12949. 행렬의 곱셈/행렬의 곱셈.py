# [
#     [1, 4],
#     [3, 2],
#     [4, 1]
#  ]	

# [
#     [3, 3],
#     [3, 3]
# ]	


def solution(arr1, arr2):
    answer = []
    
    for arr1_row in arr1:
        result_row = []
        for arr2_col in zip(*arr2):
            sum = 0
            for x, y in zip(arr1_row, arr2_col):
                sum += x * y
            
            result_row.append(sum)
        
        #행이 완성되면 결과에 넣기
        answer.append(result_row)
    
    return answer
        
