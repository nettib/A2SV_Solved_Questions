class Solution:
    def climbStairs(self, n: int) -> int:
        track = {}

        def ways(n):
            if n <= 1:
                return 1
            if n not in track:
                track[n] = ways(n - 1) + ways(n - 2)
            
            return track[n]
        
        return ways(n)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna