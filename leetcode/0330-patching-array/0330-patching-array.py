class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        x = 0
        i = 0
        patches = 0

        while x < n:
            if i < len(nums) and nums[i] <= x + 1:
                x += nums[i]
                i += 1
            else:
                x += (x + 1)
                patches += 1

        return patches