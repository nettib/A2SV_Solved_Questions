class Solution:
    def splitString(self, s: str) -> bool:
        

        def backtrack(idx, curr):
            if idx >= len(s):
                for i in range(1, len(curr)):
                    if curr[i - 1] - curr[i] != 1:
                        return False
                return len(curr) >= 2
            

            for i in range(idx, len(s)):
                val = int(s[idx: i + 1])
                curr.append(val)
                if backtrack(i + 1, curr):
                    return True
                curr.pop()
            
            return False
            
        return backtrack(0, [])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna