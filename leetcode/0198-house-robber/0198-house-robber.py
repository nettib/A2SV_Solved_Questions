class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}

        def solve(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(solve(i + 1) , nums[i] + solve(i + 2))

            return memo[i]
        
        return solve(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna