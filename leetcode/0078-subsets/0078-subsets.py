class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(idx, curr):
            ans.append(curr[:])
            if idx >= len(nums):
                return


            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna