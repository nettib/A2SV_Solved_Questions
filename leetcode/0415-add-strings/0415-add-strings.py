class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        _len = max(len(num1), len(num2))
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        
        ans = []
        r = 0
        i = 0

        while i < len(num1) and i < len(num2):
            res = str(int(num1[i]) + int(num2[i]) + r)
            r = 0

            if len(res) == 2:
                r += int(res[0])
            
            ans.append(res[-1])

            i += 1

        while i < len(num1):
            res = str(int(num1[i]) + r)
            r = 0

            if len(res) == 2:
                r += int(res[0])
            
            ans.append(res[-1])

            i += 1
        
        while i < len(num2):
            res = str(int(num2[i]) + r)
            r = 0

            if len(res) == 2:
                r += int(res[0])
            
            ans.append(res[-1])

            i += 1
        
        if r != 0:
            ans.append(str(r))
        
        return "".join(ans[::-1])





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna