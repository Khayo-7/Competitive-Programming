from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        word1str = ''.join(word1)
        word2str = ''.join(word2)

        return word1str == word2str
        # return ''.join(word1) == ''.join(word2)