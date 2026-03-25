class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []
        def backtrack(s, k):
            if len(comb) == k:
                ans.append(comb.copy())
                return
            
            for i in range(s, n + 1):
                comb.append(i)
                backtrack(i + 1, k)
                comb.pop()

        backtrack(1, k)  
        return ans
