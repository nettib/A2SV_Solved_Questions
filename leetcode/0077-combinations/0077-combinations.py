class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []
        def backtrack(start):
            if len(comb) == k:
                ans.append(comb[:])
                return

            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()
            
        backtrack(1)
        return ans

