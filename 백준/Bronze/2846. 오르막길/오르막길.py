def largest_inclination_diff(arr):
    max_diff = 0
    current_diff = 0

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff > 0:
            current_diff += diff
            max_diff = max(max_diff, current_diff)
        else:
            current_diff = 0

    return max_diff

N = input()
arr = list(map(int,input().split()))

print(largest_inclination_diff(arr))