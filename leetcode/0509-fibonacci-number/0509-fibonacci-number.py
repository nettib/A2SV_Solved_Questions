class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def f(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            if n not in memo:
                memo[n] = f(n - 1) + f(n - 2)
            
            return memo[n]
        
        return f(n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna