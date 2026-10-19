class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def t(n):
            if n == 0:
                return 0
            if  n == 1 or n == 2:
                return 1
            if n not in memo:
                memo[n] = t(n - 1) + t(n - 2) + t(n - 3)
            
            return memo[n]
        
        return t(n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna