class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        curr = []

        def backtrack(idx, _sum):
            if _sum == target:
                ans.append(curr.copy())
                return
            if _sum > target or idx >= len(nums):
                return

            curr.append(nums[idx])
            backtrack(idx, _sum + nums[idx])
            curr.pop()
            backtrack(idx + 1, _sum)
    
        backtrack(0, 0)

        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna