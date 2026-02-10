class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            num = str(num)
            for char in num:
                ans.append(int(char))
        
        return ans
