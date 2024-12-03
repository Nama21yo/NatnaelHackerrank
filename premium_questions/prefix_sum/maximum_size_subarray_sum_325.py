def max_size(nums, k):
    """
    Given an array of integers nums and an integer k, return the maximum length of a subarray that sums to k.
    If there isn't reeturn 0.
    Example 1:
    Input: nums = [1,-1,5,-2,3], k = 3
    Output: 4
    """
    n = len(nums)
    prefix_sum = {0:-1}
    current_sum = 0
    max_len = 0

    for i in range(n):
        current_sum += nums[i]
        target = current_sum - k
        if (target) in prefix_sum:
            max_len = max(max_len, i - prefix_sum[target])
        if (current_sum) not in prefix_sum:
            prefix_sum[current_sum] = i
    return max_len
 
print(max_size([1,-1,5,-2,3], 3)) # 4
print(max_size([-2,-1,2,1], 1)) # 2
print(max_size([2,0,0,0,3], 3)) # 4
