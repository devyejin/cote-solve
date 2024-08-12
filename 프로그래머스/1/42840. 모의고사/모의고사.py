from itertools import cycle

def solution(answers):
    result = []
    n = len(answers)
    
    patterns = [
        cycle([1,2,3,4,5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    
    scores = [0] * len(patterns)
    
    for answer in answers:
        for i in range(len(patterns)):
            if answer == next(patterns[i]):
                scores[i] += 1
    
    highest = max(scores)
    
    for idx, score in enumerate(scores):
        if highest == score:
            result.append(idx+1)
    
    return result