class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        _match = { 
                    "2": "abc", 
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                 }
    
        ans = []
        comb = []

        def get_all_comb(i):
            if len(comb) == len(digits):
                ans.append("".join(comb[:]))
                return
            
            for j in range(len(_match[digits[i]])):
                comb.append(_match[digits[i]][j])
                get_all_comb(i + 1)
                comb.pop()
        
        get_all_comb(0)
        return ans
            
        