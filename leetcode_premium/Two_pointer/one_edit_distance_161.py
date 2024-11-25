def one_edit_distance(s, t):
    count = 0
    i = 0
    j = 0
    n = len(s)
    m = len(t)
    while i  < n and j < m:
        if s[i] != t[j]:
            count += 1
        i += 1
        j += 1
    
    while i < n:
        if s[i] != t[j - 1]:
            count += 1
        i += 1
    
    while j < m:
        if t[j] != s[i - 1]:
            count += 1
        j += 1

    return count == 1
    

# Test cases
print(one_edit_distance("ab", "acb")) 
print(one_edit_distance("", "")) 

class Solution:
  def isOneEditDistance(self, s: str, t: str) -> bool:
    m = len(s)
    n = len(t)
    if m > n:  # Make sure that |s| <= |t|.
      return self.isOneEditDistance(t, s)

    for i in range(m):
      if s[i] != t[i]:
        if m == n:
          return s[i + 1:] == t[i + 1:]  # Replace s[i] with t[i].
        return s[i:] == t[i + 1:]  # Delete t[i].

    return m + 1 == n  # Delete t[-1].

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # If s is shorter than t, swap them to make sure s is longer or equal to t
        # This helps in reducing further checks
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)

        # Extract lengths of both strings.
        len_s, len_t = len(s), len(t)

        # There cannot be a one edit distance if the length difference is more than 1
        if len_s - len_t > 1:
            return False

        # Iterate through both strings
        for idx in range(len_t):
            # If the characters at current position are different,
            # It must either be a replace operation when lengths are same,
            # Or it must be an insert operation when lengths are different.
            if s[idx] != t[idx]:
                if len_s == len_t:
                    # The remainder of the strings after this character should
                    # be the same if it is a replace operation.
                    return s[idx + 1:] == t[idx + 1:]
                else:
                    # In case of insert operation, the remainder of the longer string
                    # starting from the next character should be the same as the 
                    # rest of shorter string starting from current character.
                    return s[idx + 1:] == t[idx:]

        # If all previous chars are same, the only possibility for one edit distance
        # is when the longer string has one extra character at the end.
        return len_s == len_t + 1