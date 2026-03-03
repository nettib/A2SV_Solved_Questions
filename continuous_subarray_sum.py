class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        track = {0: -1}

        curr = 0

        for i in range(len(nums)):
            curr += nums[i]

            rem = curr % k

            if rem in track and i - track[rem] > 1:
                return True
            if rem not in  track:
                track[rem] = i

            
        return False
