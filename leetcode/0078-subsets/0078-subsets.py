class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(idx, curr):
            if idx >= len(nums):
                ans.append(curr[:])
                return


            curr.append(nums[idx])
            backtrack(idx + 1, curr)
            
            curr.pop()
            backtrack(idx + 1, curr)

        backtrack(0, [])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna