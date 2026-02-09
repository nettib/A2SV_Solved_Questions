from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        
        for num in nums_counter.keys():
            if nums_counter[num] == 1:
                return num
    
