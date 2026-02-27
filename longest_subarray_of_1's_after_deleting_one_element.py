class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_track = {0: 0}
        longest = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_track[0] += 1
            
            while l < r and zero_track[0] > 1:
                if nums[l] == 0:
                    zero_track[0] -= 1
                l += 1
                 
            longest = max(longest, (r - l + 1) - 1)
        
        return longest
