# 가장 많은 숫자(key)의 개수 => 최솟값(step2)
# 단, 6 하고 9의 경우 갯수를 합산한 후 1/2처리(step1)
from collections import Counter
import math

number = Counter(input())
six_nine_sum = number['6'] + number['9']
number['6'] = math.ceil(six_nine_sum/2)
del number['9']

result = max(number.values())

print(result)