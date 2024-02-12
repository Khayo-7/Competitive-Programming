from typing import List

class Solution:

    def findWords(self, words: List[str]) -> List[str]:
        
        def check(word, row):

            for ch in set(list(word)):
                if not ch.lower() in row:
                    return False
            return True

        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        answer = []

        for word in words:
            if check(word, rows[0]) or check(word, rows[1]) or check(word, rows[2]):
                answer.append(word)

        return answer