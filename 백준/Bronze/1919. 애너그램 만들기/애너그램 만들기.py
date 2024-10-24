from collections import Counter

words1 = Counter(input())
words2 = Counter(input())

# print(words1-words2)
print(sum(((words1-words2)+(words2-words1)).values()))