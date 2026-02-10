class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        freq_track = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            track[num] = track.get(num, 0) + 1
            freq_track[track[num]].append(num)
        
        ans = set()

        for i in range(len(freq_track) - 1, -1, -1):
            for num in freq_track[i]:
                ans.add(num)
            if len(ans) == k:
                break
        
        return list(ans)
        
