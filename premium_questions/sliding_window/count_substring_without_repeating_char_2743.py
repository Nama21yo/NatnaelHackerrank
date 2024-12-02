from collections import defaultdict


def count_substring(s):
    count_unique = defaultdict(int)
    l = 0
    n = len(s)
    count = 0

    for r in range(n):
        count_unique[s[r]] += 1
        while l < r and count_unique[s[r]] > 1:
            count_unique[s[l]] -= 1
            if count_unique[s[l]] == 0:
                count_unique.pop(s[l])
            l += 1
        if r - l + 1 == len(count_unique):
            count += r - l + 1
    return count

print(count_substring("abcd"))
print(count_substring("ooo"))
print(count_substring("abab"))