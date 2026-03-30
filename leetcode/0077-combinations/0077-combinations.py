class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []

        def backtrack(num):
            if len(comb) == k:
                ans.append(comb[:])
                return
            
            if num > n:
                return

            comb.append(num)
            backtrack(num + 1)
            comb.pop()
            backtrack(num + 1)
    
        backtrack(1)
        return ans