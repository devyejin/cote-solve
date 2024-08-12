def solution(numbers):
    answer = []
    result = set()
    n = len(numbers)
        
    for i in range(n):
        for j in range(i+1, n):
            result.add(numbers[i] + numbers[j]) # O(n^2)

    answer = sorted(list(result)) # O(nlogn) 안에 O(n)이 발생하니  O(n^2logn)
    
    return answer