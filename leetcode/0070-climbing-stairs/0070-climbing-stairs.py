class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def ways(i):
            if i == n:
                return 1
            if i >= n + 1:
                return 0

            if i not in memo:
                memo[i] = ways(i + 1) + ways(i + 2)

            return memo[i]
    
        return ways(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna