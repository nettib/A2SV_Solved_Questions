class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_track = set(nums1)
        nums2_track = set()

        ans = []
        for num in nums2:
            if num in nums1_track and num not in nums2_track:
                ans.append(num)
                nums2_track.add(num)
        
        return ans

        
        
