class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        cand = num / 3

        if cand.is_integer():
            cand = int(cand)
            return [cand - 1, cand, cand + 1]
        
        return []
