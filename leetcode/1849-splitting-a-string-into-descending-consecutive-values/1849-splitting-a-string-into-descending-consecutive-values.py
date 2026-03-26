class Solution:
    def splitString(self, s: str) -> bool:
        path = []
        def backtrack(idx):
            if idx >= len(s):
                for i in  range(1, len(path)):
                    if path[i] + 1 != path[i - 1]:
                        return False
                return len(path) >= 2

            for i in range(idx, len(s)):
                val = int(s[idx: i + 1])
                if len(path) == 0 or val + 1 == path[-1]:
                    path.append(val)
                    if backtrack(i + 1):
                        return True
                    path.pop()
                
            return False
        
        return backtrack(0)
