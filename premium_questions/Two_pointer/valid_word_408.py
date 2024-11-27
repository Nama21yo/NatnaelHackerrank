def valid_word(word, abbr):
    n = len(word)
    m = len(abbr)
    i, j = 0, 0  # i for word, j for abbr
    
    while i < n and j < m:
        if abbr[j].isdigit():
            # Build the number from the abbreviation
            if abbr[j] == '0':  # Leading zero is invalid
                return False
            num = 0
            while j < m and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num  # Skip the corresponding characters in the word
        else:
            if i >= n or word[i] != abbr[j]:  # Check character match
                return False
            i += 1
            j += 1
    
    # Both indices should be at the end for a valid abbreviation
    return i == n and j == m

# Test cases
print(valid_word("apple", "a2e"))  # True
print(valid_word("apple", "a3"))   # False
print(valid_word("apple", "5"))    # True
print(valid_word("apple", "a1p3")) # False
