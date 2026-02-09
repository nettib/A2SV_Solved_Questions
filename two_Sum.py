class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_track = {}

        for i, num in enumerate(nums):
            if target - num in nums_track:
                return [nums_track[target - num], i]
            nums_track[num] = i
        
        
        
