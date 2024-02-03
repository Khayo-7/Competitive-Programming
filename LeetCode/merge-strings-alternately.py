class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = ''
        word1_index, word2_index = 0, 0
        word1_len, word2_len = len(word1), len(word2)

        # merge until one either word1 or word2 is out of character to merger
        while word1_index < word1_len and word2_index < word2_len:
            merged += word1[word1_index] + word2[word2_index]
            word1_index += 1
            word2_index += 1

        # merge the rest of either word1 or word2
        merged += word1[word1_index:] + word2[word2_index:]

        return merged