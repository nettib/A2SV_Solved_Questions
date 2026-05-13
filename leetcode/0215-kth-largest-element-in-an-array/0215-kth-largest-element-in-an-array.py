class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = heapq.nlargest(k, nums)

        return nums[-1]





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna