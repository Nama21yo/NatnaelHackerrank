def k_substring_no_repeat(s, k):
    l = 0
    count_char = {}
    n = len(s)
    if n < k:
        return 0
    count_substring = 0
    for r in range(n):
        count_char[s[r]] = count_char.get(s[r], 0) + 1
        while count_char[s[r]] > 1 or  r - l + 1 > k:
            count_char[s[l]] -= 1
            l += 1
        if r - l + 1 == k:
            count_substring += 1
    return count_substring
            
        
        
    
print(k_substring_no_repeat("havefunonleetcode", 5))
print(k_substring_no_repeat("home", 5))