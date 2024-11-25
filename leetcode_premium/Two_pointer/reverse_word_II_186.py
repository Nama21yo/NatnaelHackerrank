class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        This method reverses the words in the input list in-place.
      
        Parameters:
        s (List[str]): A list of characters representing a string with words
                        separated by single spaces.
        """

        def reverse_partial(section: List[str], start: int, end: int) -> None:
            """
            Helper function that reverses a substring of the list in-place.

            Parameters:
            section (List[str]): The list of characters which substring to be reversed
            start (int): The starting index of the substring
            end (int): The ending index of the substring
            """
            while start < end:
                section[start], section[end] = section[end], section[start]
                start += 1
                end -= 1

        length = len(s)
        # Initialize the starting index of the current word
        word_start = 0
        # Traverse the list of characters
        for idx in range(length):
            # If a space is found, reverse the word before the space
            if s[idx] == ' ':
                reverse_partial(s, word_start, idx - 1)
                # Update the starting index for the next word
                word_start = idx + 1
            # If end of the list is reached, reverse the last word
            elif idx == length - 1:
                reverse_partial(s, word_start, idx)
      
        # Reverse the whole modified list to get words in correct order
        reverse_partial(s, 0, length - 1)