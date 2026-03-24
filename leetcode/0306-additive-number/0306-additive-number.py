class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(index, prev1, prev2, count):
            if index == len(num):
                return count >= 3

            for j in range(index, len(num)):
                val = int(num[index: j + 1])
                if str(val) != num[index: j + 1]:
                    break
                if (prev2 == -1 or val == prev1 + prev2) and dfs(j + 1, val, prev1, count + 1):
                    return True
            
            return False


        for i in range(len(num) - 1):
            val = int(num[: i + 1])
            if str(val) != num[: i + 1]:
                break
            if dfs(i + 1, val, -1, 1): return True
        
        return False