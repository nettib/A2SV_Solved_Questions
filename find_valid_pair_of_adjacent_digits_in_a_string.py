class Solution:
    def findValidPair(self, s: str) -> str:
        track = Counter(s)

        for i in range(1, len(s)):
            if s[i - 1] != s[i] and track[s[i - 1]] == int(s[i - 1]) and track[s[i]] == int(s[i]):
                return s[i - 1: i + 1]
        
        return ""
