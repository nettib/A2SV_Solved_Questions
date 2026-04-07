class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cand = 0
        
        for word in strs:
            if cand == 0 or len(word) < len(cand):
                cand = word
        
        r = len(cand)

        for word in strs:
            for i in range(len(word)):
                if i < r and word[i] != cand[i]:
                    r = i
        
        return cand[:r]