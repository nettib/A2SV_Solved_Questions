class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        track = {0: 1}

        count = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]

            cand = curr % k

            if cand in track:
                count += track[cand]
            else:
                track[cand] = 0
            track[cand] += 1
        
        return count
