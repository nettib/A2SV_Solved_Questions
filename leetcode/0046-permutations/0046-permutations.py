class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        curr = []

        def backtrack(nums):
            if len(nums) == 0:
                ans.append(curr.copy())
                return


            for i in range(len(nums)):
                curr.append(nums[i])
                backtrack(nums[:i] + nums[i+1:])
                curr.pop()

        backtrack(nums)
        return ans




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna