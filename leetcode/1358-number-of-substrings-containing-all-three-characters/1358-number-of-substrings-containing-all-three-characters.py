class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        track = {}
        ans = 0

        l = 0
        for r in range(len(s)):
            if s[r] not in track:
                track[s[r]] = 0
            track[s[r]] += 1

            while len(track) == 3:
                ans += (len(s) - r)
                track[s[l]] -= 1
                if track[s[l]] == 0:
                    del track[s[l]]
                l += 1
            
        
        return ans
            




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna