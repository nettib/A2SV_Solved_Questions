class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans1 = [0] * len(nums)
        ans2 = [0] * len(nums)

        for i in range(1, len(ans1)):
            ans1[i] = ans1[i - 1] + nums[i - 1]


        for i in range(len(ans2) - 2, -1, -1):
            ans2[i] = ans2[i + 1] + nums[i + 1]
        
        for i in range(len(ans1)):
            ans1[i] = abs(ans1[i] - ans2[i])
        
        return ans1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna