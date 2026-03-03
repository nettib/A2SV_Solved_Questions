class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track = {0: 1}

        ans = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr - k in track:
                ans += track[curr - k]
            
            if curr not in track:
                track[curr] = 0
            track[curr] += 1
        
        return ans
