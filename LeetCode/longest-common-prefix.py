class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        s = ''
        for i in range(len(strs[0])):
            strs[0][i]
            for st in strs[1:]:
                try:
                    if strs[0][i] != st[i]:
                        return s
                except:
                    return s
            s += strs[0][i]
        return s