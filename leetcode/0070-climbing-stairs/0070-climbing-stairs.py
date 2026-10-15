class Solution:
    def climbStairs(self, n: int) -> int:
        track = {}

        def ways(i):
            if i >= n - 1:
                return 1
            if i not in track:
                track[i] = ways(i + 1) + ways(i + 2)
            
            return track[i]
        
        return ways(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna