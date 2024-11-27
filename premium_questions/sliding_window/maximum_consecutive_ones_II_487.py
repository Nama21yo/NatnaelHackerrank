# Remember to make your window k = 1 which is flipping of zero
class Solution:
  def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    n = len(nums)
    l = 0
    zeros  = 0
    k = 1 # we can flip one zero
    max_consecutive = 0 
    for r in range(n):
      if nums[r] == 0:
        zeros += 1
      while zeros > k:
        if nums[l] == 0:
          zeros -= 1
        l += 1
      if zeros <= k:
        max_consecutive = max(max_consecutive, r - l + 1)
    return max_consecutive
t1 = Solution()
print(t1.findMaxConsecutiveOnes([1,0,1,1,0]))
print(t1.findMaxConsecutiveOnes([1,0,1,1,0,1]))
      