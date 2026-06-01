class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            if target - nums[i] in track:
                return [track[target - nums[i]], i]
        
            track[nums[i]] = i


        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna