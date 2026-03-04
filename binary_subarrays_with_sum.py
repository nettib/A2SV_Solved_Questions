class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        track = {0: 1}

        ans = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]

            if curr - goal in track:
                ans += track[curr - goal]
            
            if curr not in track:
                track[curr] = 0
            
            track[curr] += 1
        
        return ans
