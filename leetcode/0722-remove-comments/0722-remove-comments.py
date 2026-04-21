class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        block = False
        temp = ""

        for i in range(len(source)):
            j = 0
            if not block:
                temp = ""

            while j < len(source[i]):
                
                if not block and j + 1 < len(source[i]) and source[i][j] == '/' and source[i][j + 1] == '/':
                    break

                
                if not block and j + 1 < len(source[i]) and source[i][j] == '/' and source[i][j + 1] == '*':
                    block = True
                    j += 2
                    continue

                
                if block and j + 1 < len(source[i]) and source[i][j] == '*' and source[i][j + 1] == '/':
                    block = False
                    j += 2
                    continue

                
                if not block:
                    temp += source[i][j]

                j += 1

            
            if not block and temp:
                res.append(temp)

        return res