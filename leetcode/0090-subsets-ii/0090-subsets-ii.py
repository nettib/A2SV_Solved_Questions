class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []

        nums.sort()

        def backtrack(idx):
            ans.append(subsets[:])
            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                if idx != i and nums[i] == nums[i - 1]:
                    continue
                subsets.append(nums[i])
                backtrack(i + 1)
                subsets.pop()

        backtrack(0)
        return ans
