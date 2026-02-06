class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)

        for num in range(n + 1):
            if num not in nums:
                return num

