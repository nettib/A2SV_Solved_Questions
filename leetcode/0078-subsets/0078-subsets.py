class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        curr = []

        def backtrack(idx):
            if idx >= len(nums):
                ans.append(curr.copy())
                return


            curr.append(nums[idx])
            backtrack(idx + 1)
            curr.pop()
            backtrack(idx + 1)

        
        backtrack(0)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna