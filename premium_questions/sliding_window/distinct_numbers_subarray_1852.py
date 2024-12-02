from collections import defaultdict
def distinict_number_subarray(nums, k):
    distinct = defaultdict(int)
    l = 0
    n = len(nums)
    ans = []
    j = 0
    for r in range(n):
        distinct[nums[r]] += 1
        if len(distinct) > k or r - l + 1 > k:
            distinct[nums[l]] -= 1
            if distinct[nums[l]] == 0:
                distinct.pop(nums[l])
            l += 1
        if r - l + 1 == k:
            ans.append(len(distinct))
    return ans

print(distinict_number_subarray([1,2,3,2,2,1,3], 3))
print(distinict_number_subarray([1,1,1,1,2,3,4], 4))
        
