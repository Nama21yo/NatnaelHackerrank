class Solution:
  def minimumOperations(self, nums: list[int]) -> int:
    l = 0
    n = len(nums)
    r = n - 1
    operation = 0
    
    while l < r:
      if nums[l] == nums[r]:
        l += 1
        r -= 1
        # Merge the right part if the left is greater
      elif nums[l] > nums[r]:
        nums[r - 1] += nums[r]
        r -= 1
        operation += 1
        # Merge the left one if the right is greater
      else:
        nums[l + 1] += nums[l]
        l += 1
        operation += 1
    return operation

t1 = Solution()
print(t1.minimumOperations([4,3,2,1,2,3,1]))
print(t1.minimumOperations([1,2,3,4]))
        
        