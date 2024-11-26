def reverse_words(word):
    i = 0
    j = 0
    n = len(word)
    while j < n:
        if word[j] == " " or j == n - 1:
            space =  j
            j = j - 1 if word[j] == " " else j
            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            i , j = space + 1, space + 1
        else:
            j += 1
    i = 0
    j = n - 1
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1
    return word  

            

print(reverse_words(["t", "h", "e"," ", "s", "k", "y", " ", "i", "s", " ", "b" , "l", "u", "e"]))
            