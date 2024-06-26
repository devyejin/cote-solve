from bisect import bisect_left, bisect_right

def count_by_range(data, left_value, right_value):
    left_index = bisect_left(data, left_value)
    right_index = bisect_right(data, right_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a,4,4)) #2

print(count_by_range(a,-1,3)) #6