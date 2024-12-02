def k_smallest_subarray(nums, k):
    l = min(nums)
    r = sum(nums)
    def checkSubArray(num):
        l = 0
        n = len(nums)
        current_sum = 0   
        count = 0    
        for r in range(n):
            current_sum += nums[r]
            while current_sum > num:
                current_sum -= nums[l]
                l += 1
            
            count += r - l + 1
        return count >= k
            


    answer  = 0
    while l <= r:
        mid = l + (r - l) // 2
        if checkSubArray(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer

    
print(k_smallest_subarray([2,1,3], 4))
print(k_smallest_subarray([3,3,5,5], 7))