class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(next, prev):
            if next == len(s):
                return True

            for j in range(next, len(s)):
                curr = int(s[next: j + 1])
                if prev - 1 == curr and backtrack(j + 1, curr):
                    return True
            return False

        for i in range(len(s) - 1):
            start = int(s[: i + 1])
            if backtrack(i + 1, start): return True
        
        return False
