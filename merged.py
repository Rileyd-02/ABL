from typing import List
def longest_equal_subarray(arr: List[int]) -> int:
    if not arr:
        return 0
    cumulative_diff = {0: -1}
    max_length = 0
    current_diff = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            current_diff -= 1
        else:
            current_diff += 1
        if current_diff in cumulative_diff:
            subarray_length = i - cumulative_diff[current_diff]
            max_length = max(max_length, subarray_length)
        else:
            cumulative_diff[current_diff] = i
    return max_length

arr1 = [0, 1, 0, 1, 1, 0, 0]
result1 = longest_equal_subarray(arr1)
print(result1)  

arr2 = [1, 0, 1, 1, 1, 0]
result2 = longest_equal_subarray(arr2)
print(result2)  

arr3 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
result3 = longest_equal_subarray(arr3)
print(result3)  