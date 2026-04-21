class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        block = 0
        temp = ""

        for i in range(len(source)):
            if not block:
                temp = ""
            j = 0
            while j < len(source[i]):

                if not block and j + 1 < len(source[i]) and source[i][j] == '/' and source[i][j + 1] == '/':
                    break
                
                if not block and j + 1 < len(source[i]) and source[i][j] == '/' and source[i][j + 1] == '*':
                    block = 1
                    j += 2
                    continue
                if block and j + 1 < len(source[i]) and source[i][j] == '*' and source[i][j + 1] == '/':
                    block = 0
                    j += 2
                    continue
                
                if not block:
                    temp += source[i][j]
                j += 1
                
            if not block and temp:
                res.append(temp)
        
        return res


