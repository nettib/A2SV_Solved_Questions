class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1


        while l <= r:
            m = l + ((r - l) // 2)
            prev = -float("inf")
            _next = -float("inf")

            if m != 0:
                prev = nums[m - 1]
            if m != len(nums) - 1:
                _next = nums[m + 1]

            if prev < nums[m] > _next:
                return m
            elif _next > nums[m]:
                l = m + 1
            else:
                r = m - 1
        

        

            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna