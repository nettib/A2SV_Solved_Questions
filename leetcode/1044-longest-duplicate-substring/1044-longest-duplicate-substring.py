class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def is_duplicate(l):
            track = set()

            for i in range(len(s)):
                if i + l > len(s):
                    return ""
                
                _s = s[i: i + l]
                if _s in track:
                    return _s
                track.add(_s)
            
        
        l = 1
        r = len(s) - 1

        ans = ""
        while l <= r:
            m = l + ((r - l) // 2)

            res = is_duplicate(m)
            if res:
                ans = res
                l = m + 1
            else:
                r = m - 1
        
        return ans
            




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna