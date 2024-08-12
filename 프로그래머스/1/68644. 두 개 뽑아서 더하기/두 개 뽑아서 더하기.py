def solution(numbers):
    answer = []
    result = set()
    n = len(numbers)
        
    for i in range(n-1):
        for j in range(i+1, n):
            result.add(numbers[i] + numbers[j]) # O(n^2)

    answer = sorted(list(result)) # O(nlogn) => end up O(nlogn)
    
    return answer