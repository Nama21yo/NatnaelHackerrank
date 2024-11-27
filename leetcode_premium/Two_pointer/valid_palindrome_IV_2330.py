def valid_palindrome_IV(s):
        count = 0
        n = len(s)
        i = (n // 2 - 1) if n % 2 == 0 else (n // 2)
        l = i
        r = i + 1 if n % 2 == 0 else i
        while l >= 0 and r < n:
            if s[l] != s[r]:
                count += 1
            l -= 1
            r += 1
        return count <= 2
print(valid_palindrome_IV("abcdef"))
print(valid_palindrome_IV("abcdba"))
print(valid_palindrome_IV("aa"))
                
class Solution:
  def makePalindrome(self, s: str) -> bool:
    change = 0
    l = 0
    r = len(s) - 1

    while l < r:
      if s[l] != s[r]:
        change += 1
        if change > 2:
          return False
      l += 1
      r -= 1

    return True
t1 = Solution()
print("Method 2")
print(t1.makePalindrome("abcdba"))       
print(t1.makePalindrome("aa"))       
print(t1.makePalindrome("abcdef")) 