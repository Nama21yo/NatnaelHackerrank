from collections import defaultdict
from math import inf

class WordDistance:
    def __init__(self, words_dict: List[str]):
        # Initializing a default dictionary to store the indices of each word
        self.indices_map = defaultdict(list)
      
        # Loop through the list of words and populate the indices map
        for index, word in enumerate(words_dict):
            self.indices_map[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        # Retrieve the list of indices for the two words
        indices_word1, indices_word2 = self.indices_map[word1], self.indices_map[word2]
        # Initialize the minimum distance to infinity
        min_distance = inf
        # Initialize two pointers for the lists of indices
        i, j = 0, 0
      
        # Iterate until we reach the end of one of the lists of indices
        while i < len(indices_word1) and j < len(indices_word2):
            # Update the minimum distance as the smaller between the previous
            # minimum distance and the current distance between word1 and word2
            min_distance = min(min_distance, abs(indices_word1[i] - indices_word2[j]))
            # Move the pointer of the list which currently has a smaller index forward
            if indices_word1[i] <= indices_word2[j]:
                i += 1
            else:
                j += 1
      
        # Return the minimum distance found
        return min_distance

# Example of usage:
word_distance = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(word_distance.shortest("coding", "practice"))
print(word_distance.shortest("makes", "coding"))