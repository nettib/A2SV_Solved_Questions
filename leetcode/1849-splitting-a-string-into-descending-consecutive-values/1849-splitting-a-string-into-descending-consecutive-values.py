class Solution:
    def splitString(self, s: str) -> bool:
        path = []
        def backtrack(idx):
            if idx >= len(s):
                return len(path) >= 2
            
            if len(path) >= 2 and path[-1] + 1 != path[-2]:
                return False
            

            for i in range(idx, len(s)):
                val = int(s[idx: i + 1])
                if len(path) == 0 or val == path[-1] - 1:
                    path.append(val)
                    if backtrack(i + 1):
                        return True
                    path.pop()
            return False
        
        return backtrack(0)
                