class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        
        return nums[l]

# [3, 1, 2]
#     m