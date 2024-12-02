from collections import defaultdict


def distinct_numbers(nums, k):
    l = 0
    n = len(nums)
    distinct = defaultdict(int)
    answer = []

    for r in range(n):
        distinct[nums[r]] += 1
        if r - l + 1 > k:
            distinct[nums[l]] -= 1
            if distinct[nums[l]] == 0:
                distinct.pop(nums[l])
            l += 1
        if r - l + 1 == k:
            answer.append(len(distinct))
    return answer
        


print(distinct_numbers([1,2,3,2,2,1,3], 3))
print(distinct_numbers([1,1,1,1,2,3,4], 4))