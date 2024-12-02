from collections import defaultdict
def unique_flavors(candies, k):
    count_unique = defaultdict(int)
    n = len(candies)
    for i in range(n):
        count_unique[candies[i]] += 1

    l = 0
    max_flavor = 0
    for r in range(n):
        count_unique[candies[r]] -= 1
        if count_unique[candies[r]] == 0:
            count_unique.pop(candies[r])
        if r - l + 1 > k:
            count_unique[candies[l]] += 1
            l += 1
        if r - l + 1 == k:
            max_flavor = max(max_flavor, len(count_unique))
    return max_flavor




print(unique_flavors([1,2,2,3,4,3], 3)) # 3
print(unique_flavors([2,2,2,2,3,3], 2)) # 2
print(unique_flavors([2,4,5], 0)) # 3